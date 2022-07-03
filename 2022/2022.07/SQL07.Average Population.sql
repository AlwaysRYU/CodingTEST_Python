# Average Population

# 문제
- 모든 도시의 평균 인구를 쿼리하기
- 도시의 인구는 가장 가까운 정수로 내림한다.

# 풀이
SELECT ROUND(AVG(POPULATION))
FROM CITY;