# Write your MySQL query statement below
SELECT new_table.dep as Department , new_table.name as Employee, new_table.salary as Salary
FROM
( 
SELECT d.name as dep,e.name as name,e.salary as salary ,DENSE_RANK() OVER(Partition by e.departmentId order by e.salary DESC) as ranking  FROM Employee e Join Department d ON d.id = e.departmentId
) as new_table
WHERE new_table.ranking <=3