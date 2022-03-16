-- Lists the number of records with the same score on the second_table
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;