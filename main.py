import argparse
import multiprocessing as mp
import sys
import threading

import progressbar
from itertools import zip_longest

import yaml

import databases

q = mp.Queue()
mutex = threading.Lock()


def grouper(n, iterable, fillvalue=None):
    """
    Collects the file data into fixed length chunks
    :param n: the number of chunks to generate
    :param iterable: the iterable object
    :param fillvalue: the fillvalue to be used in zip_longest
    :return: file contents in chunks
    """
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def process_chunk(chunk, delimiter, q, table_name):
    """
    Processes each file chunk and adds the query to the queue.
    :param chunk: the file segment to process
    :param delimiter: the delimiter to use
    :param q: the multiprocessing.queue object
    :param table_name: the name of the table defined in the YAML file
    """
    for line in chunk:
        preprocess = "', '".join(line.strip().split(delimiter))
        q.put(f"INSERT INTO {table_name} VALUES ('{preprocess}')", False)


def blocks(files, size=65536):
    """
    Auxiliary method to read the file efficiently.
    :param files: the file object
    :param size: the maximum number of bytes to read
    :return: fixed amount of bytes of the file content
    """
    while True:
        b = files.read(size)
        if not b: break
        yield b


# Command-line arguments
parser = argparse.ArgumentParser(description='Process big CSV files into SQLite databases.')
parser.add_argument("-f", "--file", help="The CSV file to process", type=str, required=True)
parser.add_argument("-w", "--max-worker-threads", help="The maximum number of concurrent processes to read "
                                                       "and process the CSV file", type=int, required=True)
parser.add_argument("-s", "--settings", help="The settings file", type=str, required=True)
parser.add_argument("-d", "--delimiter", help="The delimiter of the CSV file", type=str, default=",")
args = parser.parse_args()

# GLOBAL VARIABLES
NUM_LINES = 0
MAX_LINES_PER_THREAD = 0
MAX_WORKER_THREADS = args.max_worker_threads
FILE = args.file
SETTINGS_FILE = args.settings
DELIMITER = args.delimiter

# Reading the number of lines of the file
try:
    with open(FILE, "r", encoding="utf-8", errors='ignore') as f:
        NUM_LINES = sum(bl.count("\n") for bl in blocks(f))
except FileNotFoundError:
    print(f"There is no such file with the name '{FILE}'. Please make sure there are no typos or this is the correct "
          f"path...")
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# Reading the YAML file
try:
    with open(SETTINGS_FILE) as file:
        settings = yaml.full_load(file)
except FileNotFoundError:
    print(f"There is no such file with the name '{SETTINGS_FILE}'. Please make sure there are no typos or this is the "
          f"correct path...")
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# Creating the database table
getattr(databases, settings["database"]["type"]).create_table(settings)

MAX_LINES_PER_THREAD = NUM_LINES // MAX_WORKER_THREADS

# Shared value to calculate how many lines have been processed
num = mp.Value('i', 0)

# Initiate the processes that chunk the file into pieces
pool_processes = []
with open(FILE) as f:
    next(f)
    for i, g in enumerate(grouper(MAX_LINES_PER_THREAD, f, fillvalue=""), 1):
        pool_processes.append(mp.Process(target=process_chunk, args=(g, DELIMITER, q, settings["table-name"])).start())

# Initiate the processes that process the queue and the queries
sql_pool_processes = []
for track in range(MAX_WORKER_THREADS):
    sql_pool_processes.append(
        mp.Process(target=getattr(databases, settings["database"]["type"]).process_sql,
                   args=(q, mutex, settings, num)).start())

# Progress bar to display the current status
bar = progressbar.ProgressBar(max_value=NUM_LINES)


def print_status():
    """
    Simple timed function to update the progressbar.ProgressBar instance.
    """
    threading.Timer(5.0, print_status).start()
    bar.update(num.value)


print_status()
