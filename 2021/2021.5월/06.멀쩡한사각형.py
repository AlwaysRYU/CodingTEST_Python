# 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3
#

#올림함수 를 쓰기 위핸
import math
from fractions import Fraction

#시간초과뜸
def solution(w,h):
    answer = 0
    
    if (w==h):
        return (w*h) - w
    if w == 1 or h == 1 :
        return 0

    # 소수점 자리 전환
    kiulki = Fraction(h,w)
    print("기울기 : " + str(kiulki))

    before = 0

    for i in range(1,w+1):
        y = i * kiulki
        answer += math.ceil(round(y-before,5))
        print("현재 answer " + str(answer))
        before = math.floor(y)

        if (y - math.floor(y)) == 0:
            xx = w // i
            print("y가 정수임 탈출 , 곱할 수는 : " + str(xx))
            temp = answer * xx
            return (w*h) - temp
    
    print(w*h)
    return (w*h) - answer

from math import gcd

def solution2(w,h):
    
    if (w==h):
        return (w*h) - w
    if w == 1 or h == 1 :
        return 0

    return w*h - (w + h - gcd(w,h))

print(solution(8,12))
print(solution(6,2))
print(solution(5,3))
print(solution(3,11))

print(solution(5,4))
print(solution(10,5))
print(solution(17,23))
print(solution(3,15233730))



# assertEquals(80, test.solution(8, 12));
# assertEquals(12, test.solution(5, 4));
# assertEquals(40, test.solution(10, 5));
# assertEquals(352, test.solution(17, 23));
# assertEquals(30467460, test.solution(3, 15233730));
