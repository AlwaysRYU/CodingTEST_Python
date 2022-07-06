# African Cities

# 문제
CONTINENT가 'Africa'인 도시의 이름을 쿼리
참고: CITY.CountryCode 및 COUNTRY.Code는 일치하는 키 열입니다.

# 풀이
SELECT C.name
FROM CITY C INNER JOIN COUNTRY CT ON C.CountryCode = CT.code
WHERE CT.CONTINENT = 'Africa';