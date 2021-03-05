# Supported DBMS

- [MySQL](https://www.mysql.com/)   
- [PostgreSQL](https://www.postgresql.org/)     
- [SQLite](https://www.sqlite.org/) 

## Where is my DBMS?
This tool is very focused on popular DBMS, at the current time. Nevertheless, you are free to contribute with your favourite DBMS! Just make a pull request with your DBMS and I'll be more than happy to include it in this repository.

To start creating the DBMS wrapper for your favourite DBMS, take a look at the existing ones and create one with the same methods.

If after your implementation, you are able to upload data to the database, you're good to go!

!!!tip
    Make sure you maintain the method's signatures as they all need to be the same, across all DBMS. You can make auxiliary methods, as long as you keep them inside one `.py` file