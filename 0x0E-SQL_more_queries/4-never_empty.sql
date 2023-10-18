-- script that creates id_not_null table on MySql
-- id_not_null description
-- The database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256) );
