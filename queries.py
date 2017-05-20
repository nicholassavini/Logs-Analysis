import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")

def top_articles():
	conn = connect()
	curs = conn.cursor()
	curs.execute("""
 			 	SELECT title, COUNT(title) as views from articles_with_logs
 			 	GROUP BY title ORDER BY views DESC
 			 	""")
	articles = curs.fetchall()
	conn.commit()
	conn.close()

	return articles 

print(top_articles())