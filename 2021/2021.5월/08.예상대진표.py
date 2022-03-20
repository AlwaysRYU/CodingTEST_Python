# 예상대진표
# 

import math

# 나의풀이
def solution(n,a,b):
    answer = 1
    
    while True :
        if math.ceil(a/2) == math.ceil(b/2) :
            return answer
        else:
            a = math.ceil(a/2)
            b = math.ceil(b/2)
            answer += 1
    return answer

# 다른 사람의 풀이
def solution2(n,a,b):
    answer = 0
    while a != b: # a와 b가 다른 동안
        answer += 1
        a, b = (a+1)//2, (b+1)//2
    return answer
print(solution(8,4,7))
