# The PADS
-- https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true

# 문제 1
- OCCUPATIONS의 모든 이름을 알파벳순으로 나열한 목록을 쿼리
- 뒤에 각 직업의 첫 글자를 괄호로 묶습니다(예: 괄호로 묶음). 예: AnActorName(A), ADoctorName(D), AProfessorName(P) 및 ASingerName(S).

# 풀이
SELECT CONCAT(name, '(', substring(occupation, 1, 1), ')')
FROM Occupations
ORDER BY name, substring(occupation, 1, 1);

# 문제 2
OCCUPATIONS에서 각 직업의 발생 횟수를 쿼리합니다.
발생 항목을 오름차순으로 정렬하고 다음 형식으로 출력합니다.

# 풀이
SELECT CONCAT('There are a total of ', count(occupation), ' ', LOWER(occupation), 's.')
FROM Occupations
GROUP BY occupation
ORDER BY count(occupation), occupation