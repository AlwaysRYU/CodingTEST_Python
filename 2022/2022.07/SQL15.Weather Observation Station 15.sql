# Weather Observation Station 15

# 문제
STATION 테이블의 LONG_W 을 소수 4자리에서 반올림 하여 쿼리
- LAT_N이 가장 큰 행
- LAT_N이 137.2345 보다 작은 행들 중

# 풀이
SELECT ROUND(LONG_W,4)
FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC
LIMIT 1;