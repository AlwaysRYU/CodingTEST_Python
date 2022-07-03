# Japan Population

# 문제
- 컨트리코드가 재팬인 모든 도시의 인구를 합하여 쿼리하기

# 풀이
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = 'JPN';