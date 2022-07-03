# The Blunder

# 문제
- 0을 제거한 월급의 평균과 실제 월급의 평균의 차이를 올림한 값을 쿼리하라.

# 풀이
SELECT CEILING( AVG(Salary) - AVG( REPLACE(Salary,'0','')) )
FROM EMPLOYEES ;