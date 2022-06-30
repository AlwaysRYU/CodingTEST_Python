# Weather Observation Station 12

# 문제
station의 테이블에서 city 리스트를 쿼리하기.
1. vowel로 시작하지 않고, 동시에 끝나지 않는 city (not)
2. 중복불가. (distinct)

# 풀이 (MySQL)
SELECT DISTINCT CITY
FROM STATION
WHERE NOT CITY REGEXP '[aeiou]$' AND NOT CITY REGEXP '^[aeiou]';

# 풀이 (Oracle)
SELECT DISTINCT CITY
FROM STATION
WHERE NOT REGEXP_LIKE(CITY, '[aeiou]$') AND NOT REGEXP_LIKE(CITY, '^[AEIOU]');