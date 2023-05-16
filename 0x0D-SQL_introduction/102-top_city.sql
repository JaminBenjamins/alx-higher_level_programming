-- A scripit that displays the maximum temperature 
-- in each city in July and August in a database
SELECT city AVG(temp) as max_temp
FROM temperatures 
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY max_temp DESC
LIMIT 3;
