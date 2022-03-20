#2016년
#2021.04.09 풀이
'''
https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3

2016년 1월1일은 금요일이다.
그렇다면
a월 b일은 무슨요일 인가?
두수 a,b를 입력받아 a월b일이 무슨요일인지 리턴하는 함수를 완성하라.
SUN, MON, TUE, WED, THU, FRI, SAT
a = 5
b = 24
라면, 
5월 24요일은 화요일
TUE 를 출력한다.
단, 2016 년은 윤년이다.
2월 29일까지 있다는 뜻.
'''



mon, day = 5, 24

# 366일까지 있음

def solution(a,b):
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    
    totalday = 0
    
    for i in range(1,a) :
        if i == 2 :
            totalday += 29
        elif i in [1,3,5,7,8,10,12] :
            totalday += 31
        elif i in [4,6,9,11]:
            totalday += 30

    totalday += b
    answer = day[totalday % 7]
    return answer

#다른사람의 풀이
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
#월 리스트의 0부터 추가하기

print(solution(mon,day))

