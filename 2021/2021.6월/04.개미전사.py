# 개미전사
# P.220


changgo = [1,3,1,5]

# 나의 풀이 (재귀)
def home( A):
    if len(A) < 3:
        return A[-1]
    elif len(A) == 3:
        return max(A[0] + A[2] , A[2])
    return max(home(A[:-2]) + A[-1] , home(A[:-1]))

def solution(C):
    answer = max(home(C[:-2]) + C[-1], home(C[:-1]))
    return answer 

# 바텀업 방식
def solution2(C):
    memo = [0] * 10000
    memo[0] = C[0]
    memo[1] = max(C[0], C[1])
    for i in range(2, len(C)):
        memo[i] = max(memo[i - 1], memo[i -2] + C[i])
    
    return memo[len(C)-1]

print(solution2(changgo))