# 같은 숫자는 싫어
# 2021. 04. 13.
# level.1

'''
https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3
배열 arr가 주어진다.
배열 arr의 각원소는 숫자 0부터 9까지 이루어져있다.
배열 arr에서, 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고한다.


'''

arr1 , arr2 = [1,1,3,3,0,1,1], [4,4,4,3,3]
def solution(arr):
    answer = []

    answer.append(arr[0])
    for i in range(len(arr)):
        #0부터 시작
        if answer[len(answer)-1] != arr[i]:
            answer.append(arr[i])

    return answer
    
#다른 사람의 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

print(solution(arr1))
print(solution(arr2))