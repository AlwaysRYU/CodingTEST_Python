# 1이 될때 까지
'''
어떠한 수 N이 1이 될때까지 다음의 두 과정중 하나를 반복적으로 선택하여 수행한다. 
1. N에서 1을 뺀다.
2. N을 K로 나눈다. (단, 두번째 연산은 N이 K로 나누어 떨어질때만 선택할 수 있다.)
출력은 N이 1이 될때까지 최소 횟수를 구하는 프로그램
ex
n = 17 K=4 
일 경우. 출력값은 2
'''

# 류기탁 풀이
'''
무조건 2할 수 있을 때 2번을 실행 최소다. 고로 if절 사용
'''
#N, K 받기
N, K = map(int, input().split())

temp = N
answer = 0

while True :
    if temp == 1 : break

    if (temp % K) == 0 :
        temp = temp / K
        answer += 1
    else :
        temp = temp - 1
        answer += 1

print(answer)



# 책에 나오는 풀이
n, k = map(int, input().split())
result = 0

while n >= k :         #n이 k이상일 경우
    while n % k != 0:  #나머지가 0이 아니라면
        n-=1           #n에서 1을 뺀다. 
        result += 1    #그리고 결과에 1을 더한다.
    n //= k            #K로 나눈다.
    result += 1        #그리고 결과에 1을 더한다. 

while n > 1 :          #n이 k미만, 1초과 이는 동안
    n -= 1             #n 에서 1을빼고
    result += 1        #결과에 1을 더한다.

print(result)