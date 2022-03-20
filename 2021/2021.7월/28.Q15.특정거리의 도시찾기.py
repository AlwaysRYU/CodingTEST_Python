# 특정거리의 도시찾기
# https://www.acmicpc.net/problem/18352


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)] #초기화
print(graph)

# 모든 도로 정보 입력
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
print(graph)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N+1)
distance[X] = 0 # 출발 도시 까지의 거리는 0으로 설정한다.
# X는 출발점

# BFS 너비 우선 탐색 수행 
from collections import deque
q = deque([X]) # 맨 처음 넣기
while q :
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인한다.
    for next_node in graph[now] :
        # 방문하지 않았다면
        if distance[next_node] == -1 :
            #최단거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

print(distance)


# 최단거리 계싼
check = False
for i in range(1,N+1) :
    if distance[i] == K:
        print(i)
        check = True

if check == False :
    print(-1)