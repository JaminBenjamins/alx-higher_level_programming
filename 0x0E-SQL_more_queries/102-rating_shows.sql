-- A script that displays the rating of a show on database
SELECT `title`, SUM(`rate`) AS `rating`
    FROM `tv_shows` AS shows 
        INNER JOIN `tv_show_ratings` AS rating
        ON show.`id` = rating.`show_id`
GROUP BY `title`
ORDER BY `rating` DESC;
