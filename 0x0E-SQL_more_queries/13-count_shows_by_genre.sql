-- lists all genres and displays the number of shows linked to each
SELECT tv_genres.name                 AS genre,
       COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres,
     tv_genres
WHERE tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id, tv_genres.name
ORDER BY number_of_shows DESC