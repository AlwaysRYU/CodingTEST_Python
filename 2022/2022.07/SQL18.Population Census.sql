# Population Census

# 문제
CONTINENT가 'Asia'인 모든 도시의 인구 합계를 쿼리
참고: CITY.CountryCode 및 COUNTRY.Code는 일치하는 키 열입니다.

# 풀이
SELECT SUM(C.population)
FROM CITY C INNER JOIN COUNTRY CT ON C.CountryCode = CT.code
WHERE CT.CONTINENT = 'Asia';
