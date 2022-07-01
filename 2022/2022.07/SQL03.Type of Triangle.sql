# Type of Triangle

# 문제
세 변의 길이를 사용하여 TRIANGLES 테이블의 각 레코드 유형을 식별하는 쿼리 작성
```
Equilateral: 변의 길이가 같은 삼각형입니다.
Isosceles: 변의 길이가 같은 삼각형입니다.
Scalene: 변의 길이가 다른 삼각형입니다.
Not A Triangle: 주어진 A, B, C 값은 삼각형을 형성하지 않습니다.
```

# 풀이
SELECT CASE
    WHEN A + B > C AND A + C > B AND B + C > A THEN ( CASE
        WHEN A = B AND B = C THEN 'Equilateral'
        WHEN A = B OR A = C OR B = C THEN 'Isosceles'
        ELSE 'Scalene' END ) 
    ELSE 'Not A Triangle' END
FROM TRIANGLES;