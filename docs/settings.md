# Settings file

## File definition

The settings file is provided to the tool with the flag `-s` (or `--settings`). This will be a YAML file and you need to use the following structure with this tool:

- **`table-name`**: The name of the table that you want to put the data into.
- **`columns`**: The description of the columns.
    
    For each column:
    
    - **`name`**: The name of the column.
    - **`type`**: The type of data.
    
        !!! attention "Be careful with the data definition!"
            These data definition types **will be used to instantiate a new table**. They **must be aligned with the DBMS** you'll be using.
            
            If you want to define a primary key or a unique constraint, this will the correct place to do it.
        
- **`database`**: The description of the database.
    - **`type`**: The type of the DBMS you'll be using (`mysql`, `postgresql` or `sqlite`).
    - **`host`**: The hostname of the DBMS.
    - **`user`**: The username to access the DBMS.
    - **`password`**: The password to access the DBMS.
    - **`name`**: The name of the database to use.
    
## Example file
    table-name: data
    columns:
      - name: event_place
        type: VARCHAR(100)
      - name: event_type
        type: VARCHAR(100)
      ...
    database:
      type: mysql
      host: localhost
      user: root
      password: password
      name: datoosh