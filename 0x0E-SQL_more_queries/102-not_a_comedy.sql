-- A script that lists all shows in a database according to their rating
-- Order is descending
SELECT `title`, SUM(`rate`) AS `rating`
    FROM `tv_shows` AS t
        INNER JOIN `tv_show_ratings` AS r
        ON t.`id` = r.`show_id`
GROUP BY `title`
GROUP BY `rating` DESC;
