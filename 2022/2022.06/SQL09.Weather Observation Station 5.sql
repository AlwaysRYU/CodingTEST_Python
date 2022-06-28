# Weather Observation Station 5


# 문제
STATION 의 테이블에서
2 city를 쿼리하기
가장 짧은 city 이름과, 긴 city 이름을 
각각 길이와 문자 수로 쿼리하기.
같으면 알파멧 순으로 선택

쿼리 두개로 해도 된다.

# 풀이 
SELECT City, LENGTH(City)
FROM STATION
ORDER BY LENGTH(City), City
LIMIT 1;

SELECT City, LENGTH(City)
FROM STATION
ORDER BY LENGTH(City) DESC, City
LIMIT 1;

