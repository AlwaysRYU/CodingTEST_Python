# 다리를 지나는 트럭
# 2021.04.21
# https://programmers.co.kr/learn/courses/30/lessons/42583
'''
'''
test1 = [2,	10,	[7,4,5,6]]
test2 = [100,	100,	[10]]
test3 = [100,	100,	[10,10,10,10,10,10,10,10,10,10]]

from collections import deque

def solution(bridge, weight, truck):
    answer = 0
    #지나간 트럭
    end = []
    # 현재 다리
    bridgenow = [0 for i in range(bridge)]
    bridgenow = [0] * bridge # 시간 초과 때문에 이렇게 바꿈
    print(bridgenow)
    truckN = 0
    print("----------------시작----------------")

    sumweight =0
    abc = len(truck)

    while True :
        if len(end) == abc : break
        # 진행하기
        print("현재 시간 : " + str(answer))
        # 
        print("현재 다리의 상황 : " + str(bridgenow))
        print("남아있는 트럭 : " + str(truck))
        print("다리를 지나간 트럭 : " + str(end))
        if bridgenow[0] != 0 :
            end.append(bridgenow[0])
            sumweight -= bridgenow[0]
        
        for k in range(0,len(bridgenow)-1,1):
            bridgenow[k] = bridgenow[k+1]

        bridgenow[-1] = 0
        answer += 1
        if truckN >= abc : continue

        if (sumweight + truck[truckN] ) <= weight :
            # 현재 다리에 자리가 있고, 무게를 견딜수 있으면, 트럭이 출발한다.
            sumweight += truck[truckN]
            bridgenow[-1] = truck[truckN]
            truck[truckN] = 0
            truckN += 1
            print("트럭이 들어갔습니다! 현재 다리의 상황 : " + str(bridgenow))
    return answer

print(solution(test1[0], test1[1], test1[2]))
# print(solution(test2[0], test2[1], test2[2]))
# print(solution(test3[0], test3[1], test3[2]))
# print(solution(10,3,[1]))
'''
위 풀이는 시간초과로 실패했다.
처음에 무게를 재는 방법으로 sum을 사용했는데,
시간을 사용하는 것 같아서 sumweight 변수를 추가했다.
하지만 지금도 시간초과가 출력된다.
무엇이 문제일까.
while 안에 for 문과 if의 계속적인 사용이 문제이듯
테스트케이스 2 5 6만 시간초과가 뜬다.
새로 작성하기로했다.
'''

# 나의 풀이ㅠㅠ
def solution2(bridge, weight, truck):
    answer = 0
    RealB = [0] * bridge
    
    SumW = 0

    while True:
        temp = RealB.pop(0)
        SumW -= temp

        if len(truck) > 0 and SumW + truck[0] <= weight:
            temp = truck.pop(0)
            RealB.append(temp)
            SumW += temp
        else:
            RealB.append(0)

        if len(truck) == 0 and SumW == 0:
            answer += 1
            break
        
        answer +=1
    return answer

# 다른사람의 풀이
def solution3(bridge_length, weight, truck_weights):
    q=[0]*bridge_length
    sec=0
    while q:
        sec+=1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec
# sum을 사용했는데도 풀이성공을 했다.



            # temp = bridgenow[-1]
            # for j in range(len(bridgenow)):
            #     if j == 0 and bridgenow[j] != 0:
            #         end.append(bridgenow[j])
            #         bridgenow[j] = 0
            #         continue
                
            #     if j == len(bridgenow) -2 :
            #         bridgenow[j] = temp
            #         bridgenow[j+1] = 0
            #         break

            #     bridgenow[j] = bridgenow[j+1]
            # temp = 0
            # for i in range(len(bridgenow)-2,0 , -1):
            #     bridgenow[i] = bridgenow[i+1]
            # bridgenow[-1] = 0
        
