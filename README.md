# :rewind: Datoosh :fast_forward:

## What is Datoosh?
Datoosh is a Python tool to help you upload CSV files into SQL databases. It makes use of the multiprocessing library to open multiple connections and insert all data more efficiently.

## How can I use it?
It's very easy to start with Datoosh! First of all, make sure you have, at least, Python 3.6.

### 1 - Create your virtual environment

Start by creating your virtual environment:

- Linux:
    1. `python -m venv venv`
    2. `source venv/bin/activate`
    3. `pip install -r requirements.txt`
    
- Windows:
    1. `python -m venv venv`
    2. `venv\Scripts\activate.bat` for the regular CMD or `venv\Scripts\Activate.ps1` for Powershell
    
### 2 - Create the YAML file
You will need to use a YAML file to specify some parameters of the database that will receive the data.

### 3 - Execute it!
    python main.py [OPTIONS]
    
The options are:
- `-f` - The CSV file to process (*required*)
- `-w` - The maximum number of concurrent processes to read and process the CSV file (*required*)
- `-s` - The YAML settings file (*required*)
- `-d` - The delimiter of the CSV file (*not required - default value: ","*)

Example:
    
    python main.py -w 50 -s settings.yaml -f file.csv
