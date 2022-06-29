# Weather Observation Station 7

# 문제
station 테이블에서 city 이름을 쿼리하시오.
조건
1. a,e,i,o,u 로 끝나는 city 이름
2. 중복없음

# 풀이 (MySQL)
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '[AEIOU]$';

# 풀이 (Oracle)
SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(CITY, '[aeiou]$');