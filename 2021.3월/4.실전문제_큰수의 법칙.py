# 큰수의 법칙 
'''
문제 
주어진 수를 M번 더하여, 가장 큰 수를 만드는 법칙.
배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과할 수 없다.

입력 조건
첫째 줄에 N M K 가 주어지고, 각 자연수는 공백으로 구분한다.
'''
'''
예시 : 
2 4 5 4 6 으로 이루어진 배열이 있을 때,
M = 8 , K = 3
666 5 666 5 -> 46
'''

#n, m, k 를 공백으로 입력 받기
n, m, k =  map(int, input('숫자 세개를 입력하세요 : ').split())
#map은 input으로 받은 것을 int로 바꿔준다.

#N개의 수를 공백으로 구분하여 입력 받아, 리스트로 만들어주기
data = list(map(int, input().split()))

#입력받은 수를 정렬하기
data.sort() 

#가장 큰수와 작은수를 각각 구하기
firstbig = data[n-1]
secondbig = data[n-2]

#결과
result = 0

while True:
    #가장 큰수를 K번 더할 수 있다.
    for i in range(k):
        if m == 0 : break
        result += firstbig
        m -= 1
    # M == 0 이면 반복 탈출.
    if m == 0 : break
    result += secondbig
    m -= 1

print(result)







