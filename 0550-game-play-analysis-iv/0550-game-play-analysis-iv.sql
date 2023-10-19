# Write your MySQL query statement below
# SELECT ROUND(COUNT(Distinct a1.player_id)/(SELECT COUNT(DISTINCT player_id)FROM Activity ),2) as fraction FROM Activity a1
# JOIN Activity a2 ON a1.event_date = DATE_SUB(a2.event_date, INTERVAL 1 DAY) and a1.event_date = (SELECT MIN(event_date) FROM Activity WHERE player_id = a1.player_id) and a1.player_id = a2.player_id

SELECT ROUND(COUNT(a.player_id)/COUNT(subquery.player_id),2) as fraction FROM
(SELECT player_id , MIN(event_date) as event_date FROM Activity
group by player_id) as subquery LEFT JOIN Activity a ON
a.player_id = subquery.player_id and subquery.event_date = DATE_SUB(a.event_date, INTERVAL 1 DAY)