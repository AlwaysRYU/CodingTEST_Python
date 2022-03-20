# 3진법 뒤집기
# level.1
# 2021.04.12.
#https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3
'''
자연수 n 이 매개변수로 주어진다.
n을 3진법 상에서 앞뒤로 뒤집은 후,
이를 다시 10진법으로 표현한 수를 return 하도록
solution 함수를 완성하라.

'''

nn1 , nn2 = 45, 125


def solution(n):
    templist = []
    while n >= 1 :
        templist.append(str(n%3)) #나머지를 계속 추가
        n //= 3 

    print(templist)
    answer = "".join(templist)
    print('뒤바뀐 수 : ' + answer)
    afterten = int(answer,3)

    return afterten

# 다른 사람의 풀이
def solution2(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

print(solution(nn1))
#print(nn2)

#오늘의 파이썬 
'''
int(str,기준)
기준진수로 변환하는 파이썬의 기능.
'''