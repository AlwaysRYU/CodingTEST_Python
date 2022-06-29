# Weather Observation Station 6
https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true

# 문제
station 테이블에서 city 이름을 쿼리하시오.
조건
1. a,e,i,o,u 로 시작하는 city 이름
2. 중복없음

# 풀이 (Oracle, 정규식 사용)
SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(CITY, '^[AEIOU]');

# 풀이 ( MySQL, 정규식 사용)
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[aeiou]';

# 풀이 ( MySQL, LIKE OR )
SELECT DISTINCT CITY
FROM STATION
WHERE (CITY LIKE 'a%'
       OR CITY LIKE 'e%'
       OR CITY LIKE 'i%'
       OR CITY LIKE 'o%'
       OR CITY LIKE 'u%');
