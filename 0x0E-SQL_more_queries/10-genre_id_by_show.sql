--
SELECT s.title, t.genre_id
FROM tv_shows s
NATURAL JOIN tv_show_genres t
NATURAL JOIN tv_genres g
WHERE t.genre_id = g.id
ORDER BY s.title, t.genre_id ASC;
