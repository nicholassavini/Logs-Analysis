\c news

CREATE VIEW articles_with_authors AS
	SELECT 
	title, 
	name, 
	CONCAT('/article/', slug) as new_slug 
	FROM articles 
	INNER JOIN authors 
	ON authors.id=articles.author;

CREATE VIEW articles_with_logs AS
	SELECT
	title, 
	name
	FROM articles_with_authors
	INNER JOIN log
	ON log.path=articles_with_authors.new_slug;

CREATE VIEW log_errors AS
	SELECT  
	TO_CHAR(time, 'MM/DD/YYYY') as date, 
	CAST(SUM(CASE WHEN status='404 NOT FOUND' THEN 1 ELSE 0 END) AS real) / 
	CAST(COUNT(status) AS real) * 100 AS error_percentage
	FROM log 
	GROUP BY date
	ORDER BY date ASC;
