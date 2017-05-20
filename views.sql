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
