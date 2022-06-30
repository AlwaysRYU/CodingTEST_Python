# Higher Than 75 Marks

# 문제
students 테이블에서 학생이름을 쿼리하기.
- 75 Marks 보다 많은 점수를 받은 학생
- 각각 이름의 마지막 3글자로 정렬하기
- 만약 이름의 끝이 같다면, ID로 정렬하기

# 풀이 (MySQL)
SELECT Name
FROM STUDENTS
WHERE MARKS > 75
ORDER BY RIGHT(NAME,3), ID;

# 풀이 (Oracle)
SELECT Name
FROM STUDENTS
WHERE MARKS > 75
ORDER BY SUBSTR(NAME,-3), ID;