-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.genre AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.genre
ORDER BY number_of_shows DESC;
