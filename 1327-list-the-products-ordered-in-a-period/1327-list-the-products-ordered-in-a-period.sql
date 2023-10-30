# Write your MySQL query statement below
SELECT * FROM
 (
SELECT p.product_name,SUM(o.unit) as unit 
FROM Products as p JOIN orders as o on p.product_id = o.product_id
WHERE MONTH(o.order_date) = 2 and YEAR(o.order_date) = 2020
group by p.product_id
 ) as new_table
 where new_table.unit >=100