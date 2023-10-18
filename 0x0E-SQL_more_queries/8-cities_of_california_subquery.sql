-- script that lists all ccities of california found in database
-- You are not allowed to use the JOIN keyword
SELECT id,
name FROM cities,
WHERE state_id = (
	SELECT id FROM states
	WHERE name = California )
ORDER BY id ASC;
