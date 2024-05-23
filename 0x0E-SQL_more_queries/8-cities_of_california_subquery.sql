-- List records
SELECT id, name
  FROM cities
  WHERE states.name = 'California'
  ORDER BY id;
