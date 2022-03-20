# 음양더하기
# 2021.04.20.
# https://programmers.co.kr/learn/courses/30/lessons/76501
# lv 1

'''
어떠한 정수들이 있다.
정수들의 절댓값을 차례대로 담은 정수 배열
absolutes 와
이정수들의 부호를 차례대로 담은 
sign 이 
주어질때,
실제 정수들의 합을 구하여 return 하도록 
솔루션을 완성하라.


'''

absol1, absol2 = [4,7,12], [1,2,3]	
signs1, signs2 = [True,False,True], [False,False,True]


def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else :
            answer -= absolutes[i]

    return answer

print(solution(absol1, signs1))
print(solution(absol2, signs2))