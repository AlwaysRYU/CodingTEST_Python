# 비밀지도
# 2021.04.21.
# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
'''
암호를 해독해 지도에 비상금을 숨겨놓은 장소를 찾는다.
지도는 한변의 길이가 N인 정사각형이다. 
각칸은 " " / "#" 공백과 벽으로 이루어져 있다.
전체 지도는 두장의 지도를 겹쳐서 얻을 수있다.
어느 하나라도 벽이면 벽이고, 둘다 공백이어야만 공백이다.
지도 1과 지도 2는 각각정수배열로 암호화되어있다.
벽 부분을 1 공백부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

목표 :
비밀지도를 해독하여, #과 공백으로 구성된 문자열 배열로 출력하라.

'''

test1, test2, test3 = 5 , [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]
atest1, atest2, atest3 = 6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]

import itertools

def solution(n, arr1, arr2):
    answer = []

    # n * n 전부 돌기 
    for i in range(n):
        # 디폴트 공백 리스트 생성
        templist = [ ' ' for j in range(n)]

        temp = -1
        while arr1[i] > 0 :
            print('현재 계산하는 배열1의 수 ' + str(arr1[i]))
            if arr1[i] == 1 :
                templist[temp] = '#'
                break
            elif arr1[i] % 2 == 1 :
                templist[temp] = '#'
            temp -= 1
            arr1[i] /= 2 
            arr1[i] = int(arr1[i])
        
        temp = -1
        while arr2[i] > 0 :
            print('현재 계산하는 배열2의 수 ' + str(arr2[i]))
            if arr2[i] == 1 :
                templist[temp] = '#'
                break
            elif arr2[i] % 2 == 1 :
                templist[temp] = '#'
            temp -= 1
            arr2[i] /= 2
            arr2[i] = int(arr2[i])

        strA = "".join(templist)
        answer.append(strA)
        
    print()
    return answer

print(solution(test1, test2, test3))
print(solution(atest1, atest2, atest3))

# 다른사람의 풀이
def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer