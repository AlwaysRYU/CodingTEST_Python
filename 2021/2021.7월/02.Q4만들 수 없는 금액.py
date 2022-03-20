A1 = [3,2,1,1,9]
A2 = [3,5,7]


# 쓰는 방법
import itertools
from itertools import combinations

# 나의 풀이  
# 조합 사용한다.
def solution(S):
    answer = 1
    Number = len(S)
    Jiphap = set([])
    for i in range(1,Number):
        Su = list(itertools.combinations(S,i))
        for j in Su :
            Jiphap.add(sum(j))
    print(Jiphap)
    while True :
        if not answer in Jiphap :
            return answer
        else :
            answer += 1
# 시간이 오래걸린다.

#풀이
'''
1. 리스트를 정렬한다.
2. 1부터 1씩 더해가면서 불가능 한것을 찾는다.
'''
def solution2(Arr):
    Arr.sort()
    target = 1
    for x in Arr:
        if target < x :
            return target
        target += x

    
    
print(solution(A1))
print(solution(A2))

print(solution2(A1))
print(solution2(A2))
# 풀이
'''
나와 같다. 
전부 0으로 바꾸는 경우와, 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산한다.
횟수를 세는 방법은 내가 첫번째 썼던 방법과 유사하다.
'''