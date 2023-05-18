-- A script that lists the states in a city 
-- The result is sorted in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDR BY cities.id ASC;
