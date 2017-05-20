import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def top_items(item):
    """
    Runs the query that fetches the top items that are provided as a parameter
    """
    conn = connect()
    curs = conn.cursor()
    curs.execute("""
                SELECT {0}, COUNT({0}) as views from articles_with_logs
                GROUP BY {0} ORDER BY views DESC
                """.format(item))
    items = curs.fetchall()
    conn.commit()
    conn.close()

    return items


def high_errors():
    """Runs the query that fetches the dates where errors exceeded 1%"""
    conn = connect()
    curs = conn.cursor()
    curs.execute("SELECT date, err_pcnt FROM log_errors where err_pcnt>1")
    dates = curs.fetchall()
    conn.commit()
    conn.close()

    return dates


def print_results(results):
    """
    Prints the results of any of the queries, accepting either of the above
    functions as a parameter
    """
    items = ''
    for item in results:
        items += item[0] + ' - ' + str(item[1]) + "\n"
    return items


# Prints the answers to all of the projects questions
print("Here are the top articles, listed by views:\n")
print(print_results(top_items("title")))

print("\nHere are the top authors, listed by views:\n")
print(print_results(top_items("name")))

print("\nHere are all the dates with error percentages greater than 1%:\n")
print(print_results(high_errors()))
