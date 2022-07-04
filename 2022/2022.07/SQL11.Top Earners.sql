# Top Earners

# 문제
- 직원의 총 수입은 salry * months
- 직원중 최대 총 수입과, 최대 총 수 입을 가진 직원의 수를 출력

# 풀이
SELECT (months * salary) AS total, COUNT(*)
FROM Employee
WHERE (months * salary) = (
                SELECT MAX(months*salary)
                FROM Employee )
GROUP BY total;

# 다른 풀이
SELECT salary * months as earnings, count(*)
FROM employee
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;