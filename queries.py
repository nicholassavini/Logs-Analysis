import psycopg2
import bleach

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

print(top_items("title"))
print(top_items("name"))