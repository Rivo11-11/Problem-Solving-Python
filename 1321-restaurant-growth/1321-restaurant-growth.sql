# Write your MySQL query statement below
WITH mytable AS (
   SELECT distinct visited_on, DATE_ADD(visited_on,INTERVAL 6 DAY) as end_range FROM customer
where DATE_ADD(visited_on,INTERVAL 6 DAY) in (select visited_on from customer)
)
select m.end_range as visited_on ,sum(c.amount) as amount,ROUND(sum(c.amount)/7,2) as average_amount from Customer c JOIN
mytable m on c.visited_on between m.visited_on and m.end_range
group by m.visited_on,m.end_range

