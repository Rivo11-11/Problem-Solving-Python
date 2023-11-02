# Write your MySQL query statement below
(SELECT u.name as results FROM MovieRating m
JOIN Users u ON u.user_id = m.user_id
GROUP BY m.user_id
HAVING COUNT(movie_id) = (
    SELECT COUNT(movie_id) as max FROM 
    MovieRating
    GROUP BY user_id
    ORDER BY max DESC
    LIMIT 1 
)
Order by results
LIMIT 1 
)
UNION ALL
(
SELECT m.title as results 
FROM Movies as m 
JOIN MovieRating mr ON mr.movie_id = m.movie_id
WHERE MONTH(mr.created_at) = 2 AND YEAR(mr.created_at) = 2020
GROUP BY mr.movie_id, m.title
HAVING ROUND(AVG(mr.rating),2) = (
    SELECT ROUND(MAX(avg_rating),2)
    FROM (
        SELECT AVG(rating) as avg_rating
        FROM MovieRating
        WHERE MONTH(created_at) = 2 AND YEAR(created_at) = 2020
        GROUP BY movie_id
    ) max_avg_ratings
)
ORDER BY m.title
LIMIT 1
)

