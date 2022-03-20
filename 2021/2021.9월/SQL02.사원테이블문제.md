# 사원 테이블 SQL 문제

### 사원 테이블 EMP / 부서 테이블 DEPT
```sql
CREATE TABLE `dept` (
  `deptno` INT NOT NULL,
  `dname` VARCHAR(14) NULL,
  `loc` VARCHAR(13) NULL,
  PRIMARY KEY (`deptno`));

CREATE TABLE `emp` (
  `empno` INT NOT NULL,
  `ename` VARCHAR(10) NULL,
  `job` VARCHAR(10) NULL,
  `mgr` INT(4) NULL,
  `hiredate` DATE NULL,
  `sal` DECIMAL(7,2) NULL,
  `comm` DECIMAL(7,2) NULL,
  `deptno` INT NULL,
  `empcol` VARCHAR(45) NULL,
  PRIMARY KEY (`empno`),
  INDEX `deptno_idx` (`deptno` ASC) VISIBLE,
  CONSTRAINT `deptno`
    FOREIGN KEY (`deptno`)
    REFERENCES `dept` (`deptno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- 1. 부서위치 - CHICAGO인 모든 사원들의 / 이릅,업무,급여를 출력
SELECT *
FROM EMP E JOIN DEPT D
WHERE D.loc = 'CHICAGO';    

-- 2. 부하직원이 없는 사원의 / 사원번호, 이름, 업무, 부서번호 출력
SELECT empno, ename, job, deptno
FROM EMP E
WHERE empno  NOT IN ( SELECT mgr FROM EMP WHERE mgr IS NOT NULL );

-- 3. BLAKE와 같은 상사를 가진 사원의 이름,업무,상사번호 출력하는 SQL을 작성하세요.
SELECT *
FROM EMP E
WHERE mgr = ( SELECT mgr FROM EMP WHERE ename = "BLAKE" );

-- 4. 입사일이 가장 오래된 사람 5명을 검색하세요.
SELECT *
FROM EMP E
ORDER BY hiredate ASC
LIMIT 5;

-- 5. JONES 의 부하 직원의 이름, 업무, 부서명을 검색하세요.
SELECT E.ename, E.job, D.dname
FROM EMP E JOIN DEPT D
WHERE E.mgr = (SELECT empno FROM EMP WHERE ename = "JONES" );
    
```