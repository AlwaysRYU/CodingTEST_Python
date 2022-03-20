# 점프와 순간이동
# https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 1
    position = n

    while position != 1:
        if position % 2 == 0:
            position /= 2
        else :
            position -= 1
            ans += 1
    return ans

print(solution(1))
print(solution(5))
print(solution(6))
print(solution(5000))

#다른사람의 풀이
def solution2(n):
    return bin(n).count('1')
#일맥상통한다. / 2로 나눌 수 있다면 나누고 그 횟수를 세는 것을 캐치한다면
# 이렇게 풀수 있을 것이다.