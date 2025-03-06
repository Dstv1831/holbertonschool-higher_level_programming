-- This script lists all records from the second_table 
-- of MySQL server in descending score. Except for 
-- the column which names does not contain any value 

SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL
ORDER BY score DESC;
