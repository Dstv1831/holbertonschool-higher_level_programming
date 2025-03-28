-- lists all the cities in the database hbtn_0d_usa.
-- use the INNER JOIN to match the common elements of
-- both tables

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;