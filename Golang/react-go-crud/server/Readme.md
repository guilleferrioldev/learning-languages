### Create the database
Go to postgres and create the database
```
psql -U [your_user]
```

Create it
```
CREATE DATABASE crud;
\l
\q
```

Run the server and reopen the database
```
go run .
psql -U your_user -d crud
\d blogs
```