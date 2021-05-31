# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

# 나의풀이
def solution(brown, yellow):
    answer = []
    xy = brown + yellow
    temp = 1
    hubo = []
    while temp <= (xy//2):
        if xy % temp == 0 :
            if xy//temp < temp:
                break
            hubo.append([xy//temp, temp])
        temp += 1
    for a, b in hubo :
        if ((2*a) + (2*b) -  4 ) == brown:
            return [a,b]
    return answer


# 다른사람의 풀이
# 보통 근의 공식을 이용하더라.
# 2차방정식이 나오니까 근의공식으로 푸는 방법을 사용함
import math
def solution2(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]

    
print(solution(10,2))
print(solution(8,1))
print(solution(24,24))