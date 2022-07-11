# Weather Observation Station 19

# 문제
P1(a,c) 및 p2(b,d)를 2D 평면의 두 점으로 간주합니다.
(a,b)는 각각 북위도(LAT_N)의 최소값과 최대값이고 
(c,d)는 각각 STATION의 서부 경도(LONG_W) 최소값 및 최대값.

P1 점 P2 사이의 유클리드 거리를 쿼리하고 
4자리 십진수를 표시하도록 답의 형식을 지정합니다.



# 풀이
-- 문제 해석이 더 어렵다..
SELECT ROUND(
    SQRT(POW(MAX(LAT_N)-MIN(LAT_N),2) + POW(MAX(LONG_W)-MIN(LONG_W),2)),
    4)
FROM STATION ;