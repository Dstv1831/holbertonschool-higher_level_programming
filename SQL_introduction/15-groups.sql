-- This script lists the number of records with 
-- the same score from the second_table of MySQL server

GROUP BY score
SELECT score, COUNT(*) AS number FROM second_table
ORDER BY number DESC;
