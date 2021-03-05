# Datoosh

## What is it?

:material-database: Datoosh :material-database: is a Python :material-language-python: tool to help you upload CSV files into SQL databases.

It makes use of the multiprocessing library to open multiple connections and insert all data more efficiently.

---

Documentation: <https://migueltsantana.github.io/datoosh/>

Source code: <https://github.com/migueltsantana/Datoosh>

---

## Project layout

    databases/
        mysql.py        # The MySQL wrapper module.
        postgresql.py   # The PostgreSQL wrapper module.
        sqlite.py       # The SQLite wrapper module.
    main.py             # The main script.
    requirements.txt    # The pip dependencies of the application.