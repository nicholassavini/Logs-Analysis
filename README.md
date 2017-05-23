# Udacity Logs Analysis Project

This was the fourth project for the revised Udacity Full Stack Nanodegree. It takes an existing database with information required website views, and asks you to compile reports based around the information.

### How to Run this Project Locally
This site was written in Python 3.6, using PostgreSQL as the database.
  - Download the latest version of Python 3.6 [here](https://www.python.org/downloads/)
  - Download PostgreSQL [here](https://www.postgresql.org/download/)

With everything installed you can now fork this repo, and clone it to your machine. To import the database schema and data, run the following command from the command line ` psql -d news -f newsdata.sql`. Then run PostgreSQL from the command line using the `psql` command and use `\i views.sql` to import the necessary views. To see the report data, you can run either `python3 queries.py` or `python queries.py` depending on how Python is configured on your system.

### The SQL Views
This project depends on three different SQL views that can be seen below:

* To join articles with their authors
~~~~
CREATE VIEW articles_with_authors AS
    SELECT
    title,
    name,
    CONCAT('/article/', slug) as new_slug
    FROM articles
    INNER JOIN authors
    ON authors.id=articles.author;
~~~~

* To join articles and authors with their view counts
~~~~
CREATE VIEW articles_with_logs AS
    SELECT
    title,
    name
    FROM articles_with_authors
    INNER JOIN log
    ON log.path=articles_with_authors.new_slug;
~~~~
* To calculate the error percentages for the access logs
~~~~
CREATE VIEW log_errors AS
    SELECT
    TO_CHAR(time, 'MM/DD/YYYY') as date,
    CAST(SUM(CASE WHEN status='404 NOT FOUND' THEN 1 ELSE 0 END) AS real) /
    CAST(COUNT(status) AS real) * 100 AS err_pcnt
    FROM log
    GROUP BY date
    ORDER BY date ASC;
~~~~

These can all be created directly within PostgreSQL by running each of the above statements individually, if you don't want to use the includes SQL script.
