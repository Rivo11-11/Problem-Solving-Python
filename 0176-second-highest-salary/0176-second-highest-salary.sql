# Write your MySQL query statement below
## Using Ranking Function DENSE_Rank()
## DENSE_RANK : we will order  with repetition 
SELECT IFNULL(
  (SELECT DISTINCT salary
  FROM (
    SELECT *, DENSE_RANK() OVER (ORDER BY salary DESC) AS row_num
    FROM Employee
  ) AS new_table
  WHERE new_table.row_num = 2),
  NULL
) AS SecondHighestSalary;