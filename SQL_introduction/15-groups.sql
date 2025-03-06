-- This script lists the number of records with 
-- the same score from the second_table of MySQL server

SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
