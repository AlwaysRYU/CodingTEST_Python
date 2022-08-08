# x만큼 간격이 있는 n개의 숫자
https://school.programmers.co.kr/learn/courses/30/lessons/12954?language=java

### 유형
- 구현

### 풀이
```java
public long[] solution(long x, int n) {
        long[] answer = new long[n];
        for(int i = 0 ; i < n ; i++ ){
            answer[i] = x + ( x * i);
        }
        return answer;
    }
```