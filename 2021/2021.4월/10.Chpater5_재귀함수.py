# 재귀함수
# 20221.04.11
'''
자기자신을호출하는 함수

def recursive():
    print('재귀함수 내용')
    recursive()

recursive()

'''

def recursive_fun(i):
    #4번 반복하고 종료가 가능하다.
    if i == 4:
        return
    print(i, '번째 재귀 함수에서, ' , i+1, '번째 재귀 함수를 호출합니다.')
    recursive_fun(i +1)
    print(i, '번째 재귀 함수를 종료합니다.')
        

recursive_fun(1)


# 팩토리얼 구현

#'반복'으로 구현
def factorial(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1,n+1):
        result *= i
    return result

#'재귀'로 구현
def factorial2(n):
    if n <= 1 :
        return 1
    return n * factorial2(n-1)

print('반복으로 구현 :', factorial(5))
print('재귀으로 구현 :', factorial2(5))

# 재귀 > 반복의 장점
'''
재귀 코드가 더 간결하다.
수학의 점화식(재귀식) 을 소스로 옮겼기 때문
ex
n! = n * (n-1)!
점화식이란 : 특정한 함수를 자신보다 더 작은 변수에 대한 관계로 표현 한것
다이나믹 프로그래밍이랑 관련이 있다.
수학점화식
n이 0 혹은 1일 때 -> factorial(n) = 1
n이 1 보다 클 때 -> factorial(n) = n * fatorial(n-1)
'''


