# Weather Observation Station 14

# 문제
137.2345 보다 작은 값을 갖는 STATION의 북방 위도(LAT_N)의 최대를 쿼리합니다. 

# 풀이
SELECT TRUNCATE(MAX(LAT_N),4)
FROM STATION
WHERE LAT_N < 137.2345;