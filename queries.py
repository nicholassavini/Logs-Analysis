import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")

def top_items(item):
	conn = connect()
	curs = conn.cursor()
	curs.execute("""
 			 	SELECT {0}, COUNT({0}) as views from articles_with_logs
 			 	GROUP BY {0} ORDER BY views DESC
 			 	""".format(item))
	articles = curs.fetchall()
	conn.commit()
	conn.close()

	return articles 

def high_errors():
	conn = connect()
	curs = conn.cursor()
	curs.execute("SELECT date, err_pcnt FROM log_errors where err_pcnt>1")
	dates = curs.fetchall()
	conn.commit()
	conn.close()

	return dates


print(top_items("title"))
print(top_items("name"))
print(high_errors())