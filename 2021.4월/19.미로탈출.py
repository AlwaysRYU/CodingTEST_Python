# 미로탈출
# 2021.04.18.
'''
나의 위치는 (1,1) 이고,
미로의 출구는 (N,M)의 위치에 존재한다.
괴물의 위치는 0이고, 없으면 1이다.

'나'가 탈출하기위해 움직여야하는 칸의 개수를 구하라.

'''

# 정수를 입력받기
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의

dx = [ -1 , 1, 0 , 0 ]
dy = [ 0 , 0 , -1, 1]

from collections import deque
# bfs는 큐로 구현 하자.

def bfs(x,y) :
    # 큐선언 
    queue = deque()
    # 큐에 x y를 넣는다.
    queue.append((x,y))
    print('queue :  ' + str(queue) )
    # 큐가 빌때까지 반복한다.
    while queue:

        # x y를 꺼낸다.
        x,y = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우
            if graph[nx][ny] == 1:
                # 이걸 수를 바꿔준다.
                graph[nx][ny] = graph[x][y] + 1
                
                queue.append((nx,ny))

    return graph[n-1][m-1]


print(bfs(0,0))


