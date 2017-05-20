\c news

CREATE VIEW articles_with_authors AS
	SELECT 
	title, 
	name, 
	CONCAT('/article/', slug) as new_slug 
	FROM articles 
	INNER JOIN authors 
	ON authors.id=articles.author;