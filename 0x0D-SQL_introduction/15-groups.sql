-- script lists number of recods with same score in second_table database
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER by number DESC;
