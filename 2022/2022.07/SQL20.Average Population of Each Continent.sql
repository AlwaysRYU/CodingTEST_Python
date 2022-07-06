# Average Population of Each Continent

# 문제
- 대륙의 이름과, 인구를 쿼리
- 인구는 소수점을 버리고 정수로 출력

# 풀이
SELECT CT.Continent, FLOOR(AVG(C.Population))
FROM CITY C INNER JOIN COUNTRY CT ON C.CountryCode = CT.code
GROUP BY CT.Continent;