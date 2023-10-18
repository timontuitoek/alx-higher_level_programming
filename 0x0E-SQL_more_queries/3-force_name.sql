-- script that creates table force name on MySql
-- force_name description
-- The database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL);
