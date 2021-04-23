# 주식가격
# 2021.04.22
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
'''
prices : 초단위로 주식가격이 담긴 배열 
가격이 떨어지지않은 기간은 몇초인지 return 하도록 solution을 완성하라.


'''
# 힌트 : 스택 / 큐

from collections import deque

absol1  = [1,2,3,2,3]

# 효율성으로 실패했다.
def solution(prices):
    answer = []
    for i in range(len(prices)):    
        tempque = deque(prices[i:])
        print("이번 큐 : " + str(tempque))
        number = tempque.popleft()
        ansN = 1
        while tempque :
            #만약 크면 바로 탈출
            if tempque.popleft() < number:
                answer.append(ansN)
                break
            elif len(tempque) == 0 :
                answer.append(ansN)
                break
            ansN += 1
        
        kizun = prices[i]
        print("이번에 기준이 되는 수 " + str(kizun), end= '\n')
        ansN = 1
        

            
    answer.append(0)
    return answer

print(solution(absol1))

def solution4(prices):
    answer = [ 0 for i in range(len(prices))]
    print(answer)
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] >prices[j]:
                break
            else:
                answer[i] +=1
    return answer

print(solution4(absol1))

# 다른 사람의 풀이
# 스택을 이용한 풀이
def solution_stack(p):
    # 답 생성
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans

#밑은 고민의 흔적

# def solution2(prices):
#     answer = []
#     tempque = deque(prices)
#     i = 0
#     ansN = 0
#     while tempque:
#         if i == len(prices): break
#         print("이번 큐 : " + str(tempque))
#         kizun = prices[i]
#         temp = tempque.popleft()
#         tempque.append(temp)
#         #s넣었을 때
#         if  temp < kizun :
#             print("answer에 넣은 수 : " + ansN)
#             answer.append(ansN)
#             i += 1
#             ansN = i * (-1)
#         elif ansN == len(prices)-1:
#             answer.append(ansN)
#             i += 1
#             ansN = i * (-1)
        
#         ansN += 1

#     answer.append(0)
#     print(answer)
#     return answer

# //print(solution2(absol1))



# def solution2(prices):
#     answer = []
#     tempque = deque(prices)
#     i = 0
#     ansN = 0
#     while tempque:
#         if i == len(prices): break
#         print("이번 큐 : " + str(tempque))
#         kizun = prices[i]
#         temp = tempque.popleft()
#         tempque.append(temp)
#         #s넣었을 때
#         if  temp < kizun :
#             print("answer에 넣은 수 : " + ansN)
#             answer.append(ansN)
#             i += 1
#             ansN = i * (-1)
#         elif ansN == len(prices)-1:
#             answer.append(ansN)
#             i += 1
#             ansN = i * (-1)
        
#         ansN += 1

#     answer.append(0)
#     print(answer)
#     return answer

# def solution3(prices):
#     answer = []
#     tempque = deque(prices)

#     least = 0
#     ansN = 0
#     total = 0
#     while tempque:
        
#         total += 1
        
#         temp = tempque.pop()
#         if temp > kizun :
#             answer.append(ansN)
#             ansN = 1
        

#     answer.reverse()
#     return answer

# print(solution2(absol1))