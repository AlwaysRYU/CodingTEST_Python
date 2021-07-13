# 소수찾기

# 나의 풀이
def solution(n):
    number = n + 1
    sieve = [True] * number
    m = int(number ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            # 소수인 경우
            for j in range(i+i, number, i): 
                sieve[j] = False
    return sieve[2:number].count(True)

# 다른 사람의 풀이
def solution2(n):
    num=set(range(2,n+1)) # 집합 생성
    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
    return len(num)
# 그 뭐시깽이의 체라는 것은, 이렇게 표현 하는 것이다..
