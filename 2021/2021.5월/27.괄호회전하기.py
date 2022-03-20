# 괄호 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque 

def right(sick):
    # if s가 옳은 거면
    plus = ['(','[','{']
    minus = [')',']','}']
    zero = 0
    stack = deque()
    for j in range(len(sick)):
        if sick[j] in plus :
            stack.append(sick[j])
        else :
            if len(stack) == 0 :
                return False
            if minus.index(sick[j]) != plus.index(stack.pop()) :
                return False

    if len(stack) != 0 : return False
    return True
    
    
def solution(s) :
    answer =  0
    print("받은 문자열은 :  " + s )
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        print(temp)
        if right(temp) == True :
            answer += 1
    print("계산 끝")
    return answer 

a = "[](){}"
b = "}]()[{"
c = "[)(]"
d = "}}}"

print(solution(a))
print(solution(b))
print(solution(c))
print(solution(d))

# 다른사람의 풀이랑 비슷하다.