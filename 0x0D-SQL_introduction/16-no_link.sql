-- A script that displays the records in a table 
-- in descending order according to the score value
SELECT score, name
WHERE name IS NOT NULL
GROUP BY score DESC;
