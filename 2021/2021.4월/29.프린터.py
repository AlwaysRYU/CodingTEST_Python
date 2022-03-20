# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
'''
이 프린터의 인쇄방식은 다음과 같다.

1. 인쇄 대기 목록의 가장 앞에 있는 문서를 대기목록에서 꺼낸다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한개라도 존재하면 그것을 마지막에 넣는다.
3. 아니면 중요도가 제일 높은문서이므로 출력한다.

'''

from collections import deque

p = [[2,1,3,2], [1,1,9,1,1,1]]

def solution(priorities, location):
    answer = 1
    templist =  [[0 for j in range(2)] for i in range(len(priorities))]
    for i in range(len(priorities)):
        templist[i][0] = priorities[i]
        templist[i][1] = i
    print(templist)

    priorities.sort(reverse=True)
    maxnumber = 0
    print("최댓밗 구하기 : " + str(priorities))
    
    i = 0
    while True:
        if priorities[maxnumber] == templist[0][0] and location == templist[0][1]:
            return answer
        # 최대만 같을 때    
        elif priorities[maxnumber] == templist[0][0]:
            answer += 1
            maxnumber +=1
            del templist[0]
            print("현재 리스트 : " + str(templist) + "  프린트 한 순서는 : " + str(answer) + "  현재 최댓값 : " + str(priorities[maxnumber]))
            print("남은 최대값 리스트 " + str(priorities))

        else:
            templist.append([templist[0][0], templist[0][1]])
            print("현재 리스트 : " + str(templist) + "  프린트 한 순서는 : " + str(answer) + "  현재 최댓값 : " + str(priorities[maxnumber]))
            del templist[0]
            

    return answer

# print(solution(p[0],2))
print(solution(p[1],0))


# 다른사람의 풀이
def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# 배운거 : any, enumerate