# CH7 실전문제1 1로 만들기
# P.217
'''
정수 X를 입력받아서 1을 만들려고 한다.
정수X에 사용할 수 있는 연산은 다음과 같은 4가지 이다.
나누어 떨어질경우, 
5로 나눈다. 3으로 나눈다 2로 나눈다. 
아니면,
x에서 1을 뺀다.
연산을 사용하는 횟수의 최소값을 호출하라.
'''

def nanugi(x) :
    if ( x % 5 ) == 0:
        return x // 5
    elif ( x % 3) == 0:
        return x // 3
    elif ( x % 2 ) == 0 :
        return x // 2
    else :
        return x - 1

def solution(xx):
    answer = 0

    while True:
        if xx == 1:
            break
        else:
            print(xx)
            xx = nanugi(xx)
            answer += 1
    return answer 

print(solution(26))

# 이렇게 푸는 것이 아니다.
# 메모지에이션을 사용한다.
#

def solution2(xx):

    memo = [0] * 3000000
    # 0부터 xx까지의 답변이 가득 담긴 리스트를 만들고, 
    # 해당 값을 호출한다.

    for i in range(2, xx + 1):
        
        memo[i] = memo[i-1] + 1
        if i % 2 == 0:
            memo[i] = min(memo[i], memo[i//2] + 1 )
        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i//3] + 1 )
        if i % 5 == 0:
            memo[i] = min(memo[i], memo[i//5] + 1 )

    return memo[xx]


