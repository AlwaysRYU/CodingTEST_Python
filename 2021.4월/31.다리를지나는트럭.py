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
    print(bridgenow)
    truckN = 0
    print("----------------시작----------------")

    sumweight =0

    while len(end) < len(truck) :
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
        if truckN >= len(truck) : continue

        if bridgenow[-1] == 0 and (sumweight + truck[truckN] ) <= weight and truckN < len(truck):
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
        
