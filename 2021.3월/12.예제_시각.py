# 예제 4-2 시각
'''
정수 N이 입력되면 00시 00분 00초 부터 N시 59 59까지의 모든 시각중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

입력 : 5
출력
11475

'''
#숫자 받기

N = int(input())

count = 0
# 어차피 0부터 시작 함 

for hour in range(N + 1):
    for minute in range(60):
        for seconds in range(60):
            if '3' in str(hour) + str(minute) + str(seconds):
                count +=1

print(count)

        

