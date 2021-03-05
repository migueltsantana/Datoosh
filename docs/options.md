# CLI Options & Usage

This tool is solely a command-line (CLI) application. Follow the options below to use it correctly.

## Options

- [`-f` / `--file`](#`-f`)
- [`-w` / `--max-worker-threads`](#`-w`)
- [`-s` / `--settings`](#`-s`)
- [`-d` / `--delimiter`](#`-d`)

### `-f` 
**Required**: Yes

**Alternative flag**: `--file`    

**Description**: The CSV file to process

### `-w`
**Required**: Yes

**Alternative flag**: `--max-worker-threads`

**Description**: The maximum number of concurrent processes to read and process the CSV file

### `-s`
**Required**: Yes

**Alternative flag**: `--settings`

**Description**: The settings file

### `-d`
**Required**: No

**Alternative flag**: `--delimiter`

**Description**: The delimiter of the CSV file

**Default value**: `,`

## Usage
!!! attention "Make sure the virtual environment is activated!"
    To run this CLI, you will need some dependencies that have been previously installed. If you haven't started your installation, please consider checking [Installation](installation.md).  
    To activate your virtual environment, you just have to make sure you're on the root folder of the project and type `source venv/bin/activate`.
    
<div class="termynal" data-termynal data-termynal data-ty-typeDelay="40" data-ty-lineDelay="700">
    <span data-ty="input" data-ty-prompt="(venv) $">python main.py -w 50 -s settings.yaml -f file.csv</span>
    <span data-ty="progress"></span>
    <span data-ty>Successfully uploaded to the database</span>
</div>