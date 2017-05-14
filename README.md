# DjangoBlog

You will need to create a `db.cnf` file in the root directory with the following
structure:

```
[client]
database =
host =
user =
password = ~~
default-character-set = utf8
```

You will also need to run `makemigrations Blog` & `migrate` in order to build
the database.
