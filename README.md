# Udacity Tournament Results Project

This was the fourth project for the revised Udacity Full Stack Nanodegree. It takes an existing database with information required website views, and asks you to compile reports based around the information.

### How to Run this Project Locally
This site was written in Python 3.6, using PostgreSQL as the database.
  - Download the latest version of Python 3.6 [here](https://www.python.org/downloads/)
  - Download PostgreSQL [here](https://www.postgresql.org/download/)

With everything installed you can now fork this repo, and clone it to your machine. To import the database schema and data, run the following command from the command line ` psql -d news -f newsdata.sql`. Then run PostgreSQL from the command line using the `psql` command and use `\i views.sql` to import the necessary views. To see the report data, you can run either `python3 queries.py` or `python queries.py` depending on how Python is configured on your system.
