# Write your MySQL query statement below
# SELECT ROW_NUMBER() OVER (ORDER BY id) AS new_id, student
# FROM your_table
# ORDER BY new_id;
SELECT 
  ROW_NUMBER() OVER () AS id,
  (SELECT student FROM Seat WHERE id = sub.id) AS student
FROM 
(
  SELECT 
    IF(s.id % 2 != 0, IF(s.id = (SELECT COUNT(id) FROM Seat), s.id, s.id + 1), s.id - 1) AS id  
  FROM Seat AS s
) AS sub;