# Revising Aggregations - The Sum Function

# 문제
- 모든 도시의 인구의 합을 쿼리하기
- 캘리포니아안의 도시

# 풀이
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';