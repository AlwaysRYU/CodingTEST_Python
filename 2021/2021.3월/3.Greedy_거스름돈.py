# 예제 3-1 거스름돈
'''
동전이 500원 100원 50원 10원 있다. (개수는 무한하다.)
거슬러줘야할 돈이 N원일 때, 
거슬러줘야할 동전의 최소 개수를 구하라.
단, N은 항상 10의 배수이다.
'''

#나의 풀이
def solution(n):
    answer = 0
    
    temp = n
    coin500 = int(n/500)
    temp -= (coin500*500)
    coin100 = int(temp/100)
    temp -= (coin100*100)
    coin50 = int(temp/50)
    temp -= (coin50*50)
    coin10 = int(temp/10)

    answer = coin500 + coin100 + coin50 + coin10
    return answer

#책의 풀이
def solution2(n):
    coin_types = [500, 100, 50, 10]
    # 큰 단위의 화폐부터 차례대로 확인하기
    count = 0

    for coin in coin_types:
        count += n // coin 
        # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
        n %= coin
    
    return count 

n = 1260
print(solution(n))
print(solution2(n))

''' 
파이썬의 7가지 연산자
+ 덧셈
- 뺄셈
* 곱하기
** 거듭제곱
/ 나누기
// 나누기 연산 후 소수점이하의 수를 버리고, 정수 부분만 취함
% 나누기 연산후 몫이 아닌 나머지를 취함.
'''

'''
Greedy 
현재상황에서 가장 좋은 것만 고르는 방법이다.
'''
