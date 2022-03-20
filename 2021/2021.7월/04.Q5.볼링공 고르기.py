# 볼링공 고르기
# 1 3 2 3 2 ->

import itertools
# 나의 풀이 조합 -> 같은 것을 제거 
def solution(Arr) :
    nCr = list(itertools.combinations(Arr,2))
    print(nCr)
    i = 0
    while i < len(nCr) :
        a, b = nCr[i]
        if a == b :
            del nCr[i]
            continue
        else:
            i += 1
    return len(nCr)

print(solution([1,3,2,3,2]))
print(solution([1,5,4,3,2,4,5,2]))

# 다른 풀이 
