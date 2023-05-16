-- A script that imports another mySQL database
-- and prints the average temperature per city in descending order
SELECT CITY AVG(value) as average_temperatures
FROM temperatures
GROUP BY city
GROUP BY average_temperatures DESC;
