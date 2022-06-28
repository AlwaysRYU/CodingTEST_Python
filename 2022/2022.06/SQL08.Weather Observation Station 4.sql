# Weather Observation Station 4

# 문제
테이블에 있는 총 CITY 항목 수와
테이블에 있는 고유한 CITY 항목 수 사이의 차이를 찾으십시오.

# 풀이
SELECT ABS( COUNT( CITY ) - COUNT(DISTINCT CITY) )
FROM STATION;

