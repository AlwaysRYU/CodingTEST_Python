# SQL01
https://www.hackerrank.com/challenges/revising-the-select-query-2/problem?isFullScreen=true

# 문제
인구가 120000보다 큰 
CITY 테이블의 모든 미국 도시에 대해 
NAME 필드를 쿼리합니다. 
미국의 CountryCode는 USA입니다.


# 풀이
SQL
SELECT NAME
FROM CITY
WHERE POPULATION >= 120000 AND COUNTRYCODE = 'USA';
