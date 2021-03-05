import psycopg2


def create_connection(settings):
    """
    Creates the connection to the PostgreSQL instance.
    :param settings: the settings dictionary from the YAML file
    :return: the connection instance
    """
    try:
        conn = psycopg2.connect(
            host=settings["database"]["host"],
            user=settings["database"]["user"],
            password=settings["database"]["password"],
            database=settings["database"]["name"],
            sslmode=settings["database"]["sslmode"])
    except KeyError:
        conn = psycopg2.connect(
            host=settings["database"]["host"],
            user=settings["database"]["user"],
            password=settings["database"]["password"],
            database=settings["database"]["name"])
    return conn


def create_table_str(settings):
    """
    Creates the 'CREATE TABLE' string to initialize the database table.
    :param settings: the settings dictionary from the YAML file
    :return: the 'CREATE TABLE' string
    """
    col_struct = []
    for column in settings["columns"]:
        col_struct.append(f'{column["name"]} {column["type"]}')
    return f"CREATE TABLE {settings['table-name']} ({', '.join(col_struct)})"


def create_table(settings):
    """
    Instantiates a connection to the database and creates the table
    :param settings: the settings dictionary from the YAML file
    """
    conn = create_connection(settings)
    cursor = conn.cursor()
    cursor.execute(create_table_str(settings))
    conn.commit()
    cursor.close()
    conn.close()


def process_sql(q, mutex, settings, num):
    """
    Processes the queue and inserts the data into the database.
    :param q: the multiprocessing.queue object
    :param mutex: the threading.Lock object (only needed for SQLite)
    :param settings: the settings dictionary from the YAML file
    :param num: the mp.Value object
    """
    conn = create_connection(settings)
    cursor = conn.cursor()
    while not q.empty():
        query = q.get()
        cursor.execute(query)
        conn.commit()
        num.value += 1
    cursor.close()
    conn.close()
