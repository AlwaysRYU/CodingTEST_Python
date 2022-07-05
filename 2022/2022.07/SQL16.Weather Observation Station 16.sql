# Weather Observation Station 16

# 문제
STATION 테이블의 LAT_N 을 소수 4자리에서 반올림 하여 쿼리
- 가장 작은 LAT_N을 가진 행
- LAT_N 이 38.7780 보다 큰 행

# 풀이
SELECT ROUND(MIN(LAT_N),4)
FROM STATION
WHERE 38.7780 < LAT_N