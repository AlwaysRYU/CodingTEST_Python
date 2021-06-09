# 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911


# 나의풀이
def solution(n):
    answer = n + 1
    oneN = format(n, 'b').count('1')
    while True :
        if format(answer, 'b').count('1') == oneN :
            return answer
        answer += 1
    return answer

# 다른 사람의 풀이
def nextBigNumber(n):
    c = bin(n).count('1')
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m
# 풀이방식은 나와 똑같다.

print(solution(78))
print(solution(15))
