# 게임 맵 최단거리
# 2021.05.05.
# https://programmers.co.kr/learn/courses/30/lessons/1844?language=python3
'''
'''
maps1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
maps3 = [[1,0,0,0,0],[1,0,1,1,1],[1,1,1,0,1]]

#나의풀이
from collections import deque #deque 라이브러리 사용
def solution2(maps):
    queue = deque()
    # 가로 for 세로 -> y의 개수= 가로 / x의개수 세로
    route = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    print(route)
    
    queue.append([0,0])
    route[0][0] = 1

    # 아래 우측 위 좌측
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0,-1]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            afterx = x + dx[i]
            aftery = y + dy[i]
            if 0 <= afterx < len(maps) and 0 <= aftery < len(maps[0]) and maps[afterx][aftery] == 1 and route[afterx][aftery] == -1:
                    queue.append([afterx,aftery])
                    route[afterx][aftery] = route[x][y] + 1

    return route[-1][-1] 

# 다른사람의 풀이보다 이게 괜찮은 것 같다.
# 테이블을 하나 새로 만드는 생각이 좋은 것 같다.

print(solution2(maps1))
print(solution2(maps2))
print(solution2(maps3))



# 실패
# def solution(maps):
#     answer = 0 

#     # 아래 우측 위 좌측
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0,-1]
#     # 내 위치
#     me = [0,0]
    
#     while True:
#         stockcount = 0
#         for i in range(4):
#             afterx = me[0] + dx[i]
#             aftery = me[1] + dy[i]
#             print("현재 나의 위치 " + str(me))
            
#             if afterx < 0 or afterx > 4 or aftery < 0 or aftery > 4 or maps[afterx][aftery] == 0 :
#                 print("막혔습니다.")
#                 stockcount += 1
#                 if stockcount == 4 : return -1
#                 continue
#             else : 
#                 maps[me[0]][me[1]] = 0
#                 me[0] = afterx
#                 me[1] = aftery
#                 answer += 1
#                 break
        
#         if me == [4,4]:
#             return answer + 1
                

#     return answer


