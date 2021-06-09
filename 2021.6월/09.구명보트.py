# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

p1, l1 = [70, 50, 80, 50], 100
p2, l2 = [70, 80, 50], 100

from collections import deque

def solution(people, limit):
    answer = 0
    
    # Q = deque(people)
    # print(Q)
    while True :
        print("지금 무인도에 남은 사람 " + str(people))
        if len(people) == 0 :
            break
        elif len(people) == 1:
            return answer + 1

        M = people[0] #지금 나갈 사람
        temp = 0
        ddack = False
        for i in range(1,len(people)):
            index = 0
            if people[i] + M == limit :
                print("딱맞다!")
                del people[i]
                del people[0]
                answer += 1
                ddack = True
                break
            elif people[i] + M <= limit and people[i] > temp :
                index = i
                temp = people[i]
        
        if ddack == True :
            continue
        elif index == 0 :
            del people[0]
            answer += 1
        else :
            del people[index]
            del people[0]
            answer += 1

    return answer

print(solution(p1,l1))
print(solution(p2,l2))
print(solution([40,50,60,90], 100 ))
print(solution([160, 150, 140, 60, 50, 40], 200))


# 시간제한도 있다.
def solution2(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    print(people)
    half = int(limit / 2)
    while True :
        if len(people) == 0:
            return answer 
        elif len(people) == 1 :
            return answer + 1

        M = people[0]
        for i in range(1,len(people)):
            if people[i] + M <= limit :
                del people[i]
                del people[0]
                answer += 1
                break

    return answer

# print(solution2(p1,l1))
# print(solution2(p2,l2))
# print(solution2([40,50,60,90], 100 ))
# print(solution2([160, 150, 140, 60, 50, 40], 200))
