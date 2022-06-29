# Weather Observation Station 8

# 문제
station 테이블에서 city 이름을 쿼리하시오.
조건
1. a,e,i,o,u 로 끝나는 city 이름
2. 1의 조건과 동시에 a,e,i,o,u 로 시작하는 city 이름
3. 중복없음

# 풀이 (MySQL)
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '[aeiou]$' and CITY REGEXP '^[aeiou]';

# 풀이 (Oracle)
SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(CITY, '[aeiou]$') AND REGEXP_LIKE(CITY, '^[AEIOU]');