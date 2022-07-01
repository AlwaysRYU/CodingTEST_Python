# Employee Salaries

# 문제
employee 테이블에서 names를 출력한다.
- 월 급여가 2000 이상인 직원
- 10개월 미만으로 근무한 직원
- id 오름 차순으로 정렬

# 풀이 (MySQL)
SELECT name
FROM employee
WHERE salary >= 2000 
    AND months < 10
ORDER BY employee_id ASC;