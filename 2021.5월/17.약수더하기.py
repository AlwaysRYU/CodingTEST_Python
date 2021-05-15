# 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884?language=python3


def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        print("계산할 수 : " + str(i))
        yak = 0
        for j in range(1,i+1):
            if i % j == 0:
                yak += 1
        
        if yak % 2 == 0:
            print("약수개수 짝수")
            answer += i
        else:
            print("약수개수 홀수")
            answer -= i

    return answer

import math

def solution2(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i

    return answer

print(solution(13,17))
print(solution(24,27))