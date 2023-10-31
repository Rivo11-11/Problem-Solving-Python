# Write your MySQL query statement below
SELECT new_table.product_id,new_table.year as first_year , new_table.quantity ,new_table.price FROM
(
SELECT s.* ,DENSE_RANK() over(partition by p.product_id  order by s.year ) as ranking

 FROM Sales as s JOIN  Product as p   ON
s.product_id = p.product_id
) as new_table
where new_table.ranking = 1