-- script that lists all genres from hbtn_0d_tvshowsand displays mumber of-- shows linked to each
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
