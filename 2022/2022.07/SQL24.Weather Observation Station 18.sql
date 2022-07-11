# Weather Observation Station 18

# 문제
a는 북위도(STATION의 LAT_N)의 최소값과 같습니다.
b는 서부 경도(STATION의 LONG_W)의 최소값과 같습니다.
c는 북위도(STATION의 LAT_N)의 최대값과 같습니다.
d는 서부 경도(STATION의 LONG_W)의 최대값과 같습니다.
점 사이의 맨해튼 거리를 쿼리하고 소수점 이하 자릿수로 반올림합니다.

# 이렇게는 안된다.
SELECT ABS( ROUND( MIN(LAT_N)- MIN(LONG_W),4 ) + ABS(ROUND(MAX(LAT_N)- MAX(LONG_W) ,4)
FROM STATION;


# 풀이
-- 라운드를 위로 해줘야함
SELECT ROUND(ABS(MIN(LAT_N) - MAX(LAT_N)) + ABS(MIN(LONG_W) - MAX(LONG_W)) ,4)
FROM STATION;