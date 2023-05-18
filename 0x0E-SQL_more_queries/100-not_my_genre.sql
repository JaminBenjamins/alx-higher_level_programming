-- A script that displays the genre of a show with exception of Dexter show
SELECT DISTINCT `name`
    FROM `tv_genres` AS genre
    INNER JOIN `tv_show_genres` AS all_genres
    ON genre.`id` = all_genres.`genre.id`

    INNER JOIN `tv_shows` AS `shows`
    ON all_genres.`show_id` = shows.`id`
    WHERE genre.`name` NOT IN
        (SELECT `name`
            FROM `tv_genres` AS genre
            INNER JOIN `tv_show_genres` AS all_genres
            ON genre.`id` = all_genres.`genre_id`

            INNER JOIN `tv_shows AS shows
            ON all_genres.`id` = shows.`id`
            WHERE shows.`title` = "Dexter")
    ORDER BY genre.`name`;
