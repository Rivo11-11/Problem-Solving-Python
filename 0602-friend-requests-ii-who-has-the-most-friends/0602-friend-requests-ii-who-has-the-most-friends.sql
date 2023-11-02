# Write your MySQL query statement below
WITH a AS (
  SELECT requester_id AS id FROM RequestAccepted
  UNION ALL
  SELECT accepter_id AS id FROM RequestAccepted
)

SELECT a.id, COUNT(a.id) AS num
FROM a
GROUP BY a.id
HAVING COUNT(a.id) = (
  SELECT COUNT(a.id) AS max_count
  FROM a
  GROUP BY a.id
  ORDER BY max_count DESC
  LIMIT 1
);
