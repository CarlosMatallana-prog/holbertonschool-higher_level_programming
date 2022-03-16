-- Lists all the cities of California that can be found
SELECT cities.id, cities.name
FROM cities,
     states
WHERE states.name = 'California'