-- Write your PostgreSQL query statement below
SELECT E1.name as "Employee"
FROM Employee as E1
LEFT JOIN Employee as E2
ON E1.managerId = E2.id
WHERE E1.salary > E2.salary;