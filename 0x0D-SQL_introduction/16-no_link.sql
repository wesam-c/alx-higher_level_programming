--  lists all records of 'second_table' of the database hbtn_0c_0
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;