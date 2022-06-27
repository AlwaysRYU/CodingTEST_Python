# SQL 05
https://www.hackerrank.com/challenges/japanese-cities-name/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

# 문제
CITY 테이블에 있는 모든 일본 도시의 이름을 쿼리합니다.
일본의 COUNTRYCODE는 JPN입니다.

# 풀이
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'JPN';