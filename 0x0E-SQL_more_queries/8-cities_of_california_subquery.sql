-- A script that lists all the cities that can be found in California
SELECT id, name
FROM cities 
WHERE state_id = (SELECT id FROM state WHERE name = 'California')
ORDER BY id ASC;
