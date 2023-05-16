-- A script that displays a score >= 10 
-- and name in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
