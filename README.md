# DjangoBlog

> This project uses MySQL for the database but it is not a requirement. The following
instructions are to set up your MySQL configuration.

You will need to create a `db.cnf` file in the root directory with the following
structure:

```
[client]
database =
host =
user =
password =
default-character-set = utf8
```

You will also need to run `makemigrations Blog` & `migrate` in order to build
the database.
