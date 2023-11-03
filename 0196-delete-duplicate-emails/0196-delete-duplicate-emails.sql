/* Write your T-SQL query statement below */
WITH ranked_table AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS ranking
   FROM Person
)
DELETE FROM ranked_table WHERE ranking > 1;