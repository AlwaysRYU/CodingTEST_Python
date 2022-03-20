# 피보나치수
# https://programmers.co.kr/learn/courses/30/lessons/12945

import sys
sys.setrecursionlimit(2500)

def pivo(A) :
    if A == 0 :
        return 0
    elif A == 1 :
        return 1
    else :
        return pivo( (A-1) % 1234567 ) + pivo( (A-2) % 1234567 )


def solution(n):
    answerlist = [0 for i in range( 1234567 )]
    n = n % 1234567
    print(n)
    for i in range(1, 1234568):
        answerlist[i-1] = pivo(i)
    return answerlist[n-1] 


# 시간초과 뜬다.
# 특이사항 : 피보나치 결과를 1234567 로 나눈 나머지를 출력하는것
# 뭔가 규칙이 있는 듯?


# print(solution(3))
print(solution(5))