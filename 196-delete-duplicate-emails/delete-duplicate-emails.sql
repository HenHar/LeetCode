-- Write your PostgreSQL query statement below
DELETE FROM Person 
WHERE id NOT IN
(SELECT min(id) FROM Person
Group By email);