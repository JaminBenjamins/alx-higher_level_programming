-- A script that clusters records with similar values
SELECT score COUNT (*) as `number`
FROM `second_table` 
GROUP BY `score`
GROUP BY `number` DESC;
