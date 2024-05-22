-- Display top 3
SELECT city, AVG(value) as avg_temp
  FROM temperatures
  WHERE month = 07 OR month = 08
  GROUP BY city
  ORDER BY avg_temp DESC
  LIMIT 3;
