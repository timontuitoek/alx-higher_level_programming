-- script that lists all ccities of california found in database
-- states table contains only one record where name = California (but the id can be different, as per the example)
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id FROM states,
	WHERE name = California)
	ORDER BY id;
