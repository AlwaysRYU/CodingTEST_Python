# SQL 문제

### DB : countryDB
DDL,DML 실습

```SQL
SELECT @@autocommit;
SET autocommit = false;
SELECT @@autocommit;

SELECT sum(LifeExpectancy) '합계', round(avg(LifeExpectancy),2) '평균', MAX(lifeexpectancy) '최대', MIN(lifeExpectancy)' 최소'
FROM country;

-- # 그룹바이 continent 별 국가의 개수와 인구의 합을 구하기
SELECT Continent, count(code), SUM(Population)
FROM country
GROUP BY Continent;


-- #  대륙별 국가 표면적의 합을 구한다.
SELECT Continent, sum(SurfaceArea)
FROM country
GROUP BY CONTINENT
ORDER BY 2
LIMIT 3;

-- # 인구가 5천만 이상인 나라의 GNP 총합을 구한다. / 합으로 오름차순 정렬 // GNP총합이 얼마 이상만 출력
SELECT Continent, name, sum(GNP)
FROM country
WHERE Population >= 50000000 
GROUP BY Continent
HAVING SUM(GNP) >= 5000000
order by SUM(GNP) ASC;
-- HAVING 결과를 한번더 



-- # 연도별로 10개 이상의나라가 독립한 해는 언제인가
SELECT indepyear, count(code)
FROM country
WHERE IndepYear IS NOT NULL
GROUP BY IndepYear
HAVING count(code) >= 10;

-- # 국가별 GNP / 전세계 평균 GNP / 대륙평균 GNP 출력
-- 풀어서 보여주는것 집대성의 결과를 옆에 붙인다.
SELECT CONTINENT, name, gnp, 
	AVG(GNP) OVER(),
    AVG(GNP) OVER( partition by Continent)
    -- 평균을 내고 그룹바이 처럼 대륙별로 보여준다.
FROM country;

-- 중복의 경우  1 2 2 4 이렇게 됨
SELECT id, name , Population, RANK() OVER( ORDER BY population )
FROM CITY;

-- # countrylanguage 테이블에  값을 추가하기
SELECT *
 FROM countrylanguage;

INSERT INTO countrylanguage
	VALUES ('KOR','외계어','F',10);
-- 1452 오류남  countrycode에 AAA가 없기 때문이다.
-- 먼저 country에 값이 있어야함
SELECT *
FROM country
WHERE code = 'KOR';
SELECT * FROM countrylanguage WHERE CountryCode = "KOR";

-- # country language에 해당 값을 추가하라. 
SELECT * 
FROM countrylanguage 
WHERE CountryCode = "ABW";
INSERT INTO countrylanguage VALUES ('ABW','Dutch', 'F', 10);
-- # 듑낫다라고 하다. Dup 중복됐다는 것이다. 여기선 Dutch가 중복임 PK라서
SELECT * 
FROM countrylanguage 
WHERE CountryCode = "ABW"
AND Language = "Dutch";
INSERT INTO countrylanguage VALUES ('ABW','Dutch2', 'F', 10);


# country에 자료를 추가하기
INSERT INTO country(code, name, region, code2) 
	VALUES ('TTT','test', 'Tregion','TC');
-- 오류 1406 입력데이터가 너무 길다. 
-- 오류 1364 칼람에 디펄트 벨류가없다. NOT NULL인데 디폴트값이 없다.
SELECT *
FROM country;

# city에서 2331인 자료의 인구를 10% 증가 시키는 쿼리
UPDATE city 
	SET population = population * 1.1
    WHERE ID = 2331;

SELECT *
FROM city
WHERE ID = 2331;

# 삭제하기 
DELETE FROM country
WHERE CODE = 'USA';
-- 오류 부모쪽에서 삭제가안됨
SELECT * FROM city WHERE countryCode= 'USA';

-- #
SELECT * 
FROM countrylanguage




```