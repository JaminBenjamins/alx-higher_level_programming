-- A script that displays maximum temperature of each state
SELECT city MAX(`value`) AS `max_val`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
