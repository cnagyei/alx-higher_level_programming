-- List records
SELECT id, name
  FROM cities
  WHERE states.id = 1
  ORDER BY id;
