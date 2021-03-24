# 실전문제 숫자카드게임
'''
숫자가 쓰인 카드들이 n * m 형태로 놓여있다.
n은 행, m은 열의 개수이다.
행을 먼저 선택하여 그 카드중 가장 숫자가 낮은 카드를 뽑아야한다.
최정적으로 가장 높은 숫자가 쓰인 카드를 뽑는것이 승리 조건이다. 
'''
'''
입력 예시

3 3
3 1 2 
4 1 4
2 2 2
출력 : 2 
'''
#류기탁 풀이
n, m = map(int, input('행과 열을 입력하세요 : ').split())

for i in range(n):
    data = list(map(int, input().split()))
    temp =[]
    temp.append(min(data))
    result = max(temp)

print(result)
    
#해설풀이

n , m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data :
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)