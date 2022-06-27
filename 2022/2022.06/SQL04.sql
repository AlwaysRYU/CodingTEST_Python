# SQL 04
https://www.hackerrank.com/challenges/select-by-id/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

# 문제
CITY 테이블에 있는 모든 일본 도시의 모든 속성을 쿼리합니다.
일본의 COUNTRYCODE는 JPN입니다.
CITY 테이블은 다음과 같이 설명됩니다.

# 풀이
SELECT *
FROM CITY
WHERE COUNTRYCODE = 'JPN';
