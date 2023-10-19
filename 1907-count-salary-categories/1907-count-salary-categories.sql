# Write your MySQL query statement below
SELECT sub2.category,COUNT(sub1.category) as accounts_count FROM
(SELECT *,
  CASE
    WHEN income > 50000 THEN 'High Salary'
    WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
    ELSE 'Low Salary'
  END AS category
FROM Accounts) as sub1  RIGHT JOIN
(SELECT category
FROM (
  SELECT 'Low Salary' AS category
  UNION ALL
  SELECT 'Average Salary'
  UNION ALL
  SELECT 'High Salary'
) AS subquery) as sub2 ON sub1.category = sub2.category
GROUP BY sub1.category