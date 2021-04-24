# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899
'''
124 나라는 자신만의 숫자 변환을 한다.
n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution을 작성하라.

'''

a = [1,2,4,11,12,14,21,22,24,41,42,44,111,112,124,121,122]

list124 = [1,2,4]

def solution(n):
    answer = ""
    moak = 0
    while n :
        if n <= 3 : answer += str(n)
        answer += str(n%4)
        moak += 1
        n = (n//3)

    answer.replace('3','4',moak)    
    return answer[::-1]

def solution2(n):
    answer = ""
    moak = 0
    m = n -1
    while m > 0:
        print("현재 m : " + str(m))
        print("현재 answer : " + str(answer))
        answer += str(m % 3)
        m //= 3
        moak += 1

    answer.replace('01','4')    
    return answer[::]

# 다른사람의 풀이
def solution3(n):
    result = []
    i = 0
    
    while n > 0:
        d = 3 ** i # 3의 i 제곱
        while (n-d) % 3 ** (i + 1) != 0:
            d += 3 ** i
        result.append( d // 3 ** i)
        n = n-d
        i += 1

    return "".join(map(str,[4 if i==3 else i for i in result][::-1]))
print(solution2(10))