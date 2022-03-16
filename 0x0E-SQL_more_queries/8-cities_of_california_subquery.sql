-- Lists all the cities of California that can be found
SELECT cities.id, cities.name
FROM cities,
     states
WHERE state_id = states.id
  and states.name = 'California'