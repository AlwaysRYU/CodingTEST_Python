# Population Density Difference

# 문제
- 인구가 가장 많은 도시와 적은도시의 차이를 쿼리하기.

# 풀이
SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY;