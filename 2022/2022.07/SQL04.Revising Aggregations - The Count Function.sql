# Revising Aggregations - The Count Function

# 문제
도시의 수를 쿼리하기
- 100,000 이상의 인구를 가진 도시

# 풀이
SELECT COUNT(*)
FROM CITY
WHERE POPULATION >= 100000;