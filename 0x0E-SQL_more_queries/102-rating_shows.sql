-- Lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT tv_shows.title AS title, SUM(tv_show_ratings.rate) AS rating
  FROM tv_shows
  JOIN tv_shows
    ON tv_shows.id = tv_show_ratings.rate
  GROUP BY title
  ORDER BY rating DESC;
