# Weather Observation Station 13

# 문제
38.7880 보다 크고 137.2345작은 값을 갖는 STATION의 북방 위도(LAT_N) 합계를 쿼리합니다. 
소수점 4 이하 자릿수까지 답을 자릅니다.

# 풀이
SELECT TRUNCATE(SUM(LAT_N),4)
FROM STATION
WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;