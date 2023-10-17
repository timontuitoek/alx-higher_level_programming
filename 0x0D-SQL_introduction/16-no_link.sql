-- script that lists all records of second_table database
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
