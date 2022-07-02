# Revising Aggregations - Averages

# 문제
- 모든 도시의 인구의 평균을 쿼리하기
- 캘리포니아안의 도시

# 풀이
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';