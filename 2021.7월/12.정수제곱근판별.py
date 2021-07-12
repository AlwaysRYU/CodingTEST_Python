# 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934

# 나의 풀이
def solution(n):
    temp = 1
    while(True) :
        Number = temp * temp 
        if Number == n :
            return (temp + 1) * (temp + 1)
        elif Number > n :
            return -1
        else :
            temp += 1


# 다른사람의 풀이
def nextSqure(n):
    sqrt = n ** (1/2) # 루뜨 하는 방법..
    print(sqrt)
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'

nextSqure(121)
nextSqure(122)
