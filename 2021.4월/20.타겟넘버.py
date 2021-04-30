# 타겟넘버
# 2021.04.19.
# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
'''
n개의 음이 아닌 정수가 있다.
이를 적절히 더하거나 빼서 타겟넘버를 만드려고 한다.

예를 들어, 11111 숫자 3을 만들려면 다음 다섯방법을쓸수있다.

-1 +1 +1 +1 +1 
+1 -1 +1 +1 +1
+1 +1 -1 +1 +1
+1 +1 +1 -1 +1
+1 +1 +1 +1 -1

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성하라.
'''

n = [1,2,3,4,5]
terget = 3

from collections import deque

# BFS를 이용한다.
def solution(numbers, target):
    answer = 0

    queue = deque([(0, 0)]) # sum, level
    print("처음 큐 : " + str(queue) + '\n')

    # 큐가 빌때까지 반복한다.
    while queue:
        s, l = queue.popleft()
        # S는 총합
        # L은 numbers를 불러오기위한 수

        # l이 numbers의 크기를 벗어나면 반복문 종료.
        if l > len(numbers):
            break
        
        # l이 numbers의 길이와 같고 AND 구하는수와 s가 같다면
        elif l == len(numbers) and s == target:
            # 답에 1을 추가한다.
            answer += 1

        queue.append((s + numbers[l-1], l+1))
        queue.append((s - numbers[l-1], l+1))
        
        print("l : " + str(l) + "  현재 큐 : " + str(queue) + '\n' )

    return answer


def  solution2(numbers, target) :
    answer = 0
    # BFS는 큐로 구현한다.
    queue2 = deque([(0,0)])
    while queue2:
        Sum, Level = queue2.popleft()
        if Level > len(numbers):break
        elif Level == len(numbers) and Sum == target:
            answer += 1
            
        queue2.append((Sum + numbers[Level-1], Level+1))
        queue2.append((Sum - numbers[Level-1], Level+1))
    return answer

# 다른사람의 풀이
def solution3(numbers, target):
    # 리스트가 비었고 AND 타겟이 0이라면 #즉 조건이 맞다면 answer += 1
    if not numbers and target == 0 :
        return 1
    #리스트가 비었다면
    elif not numbers:
        return 0
    else:
        # 첫번째거 -> solution( numberlist 1부터 끝까지 , 목표 점수 - 첫번재 수 )
        # 첫번째거 -> solution ( numberlist 1부터 끝까지 , 목표 점수 + 첫번재 수 )
        return solution3(numbers[1:], target-numbers[0]) + solution3(numbers[1:], target+numbers[0])
    
print()
print("답은 : ")
print(solution(n,terget))