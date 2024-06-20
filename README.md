# transport-sqlite 

Setup the Information Management (Public transportation routes) database in SQLite

SQLite just stores the database as a file: life is easy. And so our database, with all the data already imported, can be stored just as a file in the directory `transport.db`

Check the [documentation](https://www.sqlite.org/index.html) and for installation (but I think it's pre-installed with python). The commands are straightforward. Accessing the database and running queries can all be done in the shell.

Assuming you're in the directory's shell. To go into the database, which already exists in the directory, just run from the shell:

```
> sqlite3 transport.db
```

Now, you're in the SQLite shell. To list all the tables in the database

```
sqlite> .tables
```
 
you can now run SQL queries within the shell

```sql
sqlite> SELECT * FROM routes;
```

## Create the database from scratch

All the `.csv` files are in the `data` directory so we can manually create the database, create the tables, and import the data from the files

Assuming `transport.db` does not exist, we can then create it in our directory
```
> sqlite3 transport.db
```

Then, we can read from our `tables_sqlite.sql` the SQL commands to create the tables

```
sqlite> .read tables_sqlite.sql
```

To import the data for the four tables

```
sqlite> .import "data/routes_data.csv" routes
sqlite> .import "data/operators_data.csv" operators
sqlite> .import "data/components_data.csv" components
sqlite> .import "data/vehicles_data.csv" vehicles
```

Life is good

## Check that mock data is good

We check through `validate_data_sqlite.sql` if our data for the `operators` number of operational units matches the number of vehicles in `vehicles` with the same operator. Also, we must check that the vehicle type owned by the operator matches their occupation

## SQL queries

TODO

```sql
-- Some query on the routes table with LIKE for a specific place's name

-- JOIN query on operators and vehicles

-- JOIN query on routes covered by an operator

```