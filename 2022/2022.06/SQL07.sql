# SQL 07

# 문제
station 테이블의 city 이름을 쿼리한다.
id 는 짝수여야하고, ( MOD(a,b) )
순서는 상관없다. 단,
중복은 제거해야한다.  ( DISTINCT )

# 풀이
SELECT DISTINCT CITY
FROM STATION
WHERE ( MOD(ID,2) = 0);