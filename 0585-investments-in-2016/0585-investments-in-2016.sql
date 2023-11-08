# Write your MySQL query statement below

WITH tiv_counts AS (
    SELECT tiv_2015, COUNT(*) as count_tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
)
SELECT ROUND(SUM(mytable.tiv_2016),2) AS tiv_2016
FROM (
    SELECT i1.*, i2.pid AS new
    FROM Insurance i1
    LEFT JOIN Insurance i2 ON i1.lat = i2.lat AND i2.lon = i1.lon AND i1.pid != i2.pid
    JOIN tiv_counts t ON t.tiv_2015 = i1.tiv_2015 and t.count_tiv_2015 > 1
) AS mytable 
WHERE mytable.new IS NULL 

    
