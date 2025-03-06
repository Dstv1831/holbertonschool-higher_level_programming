-- This script list all record with a score >= 10
-- from the second_table of MySQL server

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC ;