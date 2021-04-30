# 탐색알고리즘 DFS/BFS
# 2021.04.16.
'''
스택, 큐, 재귀함수는 DFS/BFS에서 가장 중요한 개념.
'''
# 그래프
'''
Node 노드 와 Edge 간선으로 표현되며, 이때 노드를 Vertex정점 이라고도 말한다.
인접하다 = 두 노드가 간선으로 연결되어 있다.
인접행렬 : 
    2차원 배열에 각 노드가 연결된 형태를 기록하는 방식이다.
    모든 관계를 저장하므로 메모리 낭비
인접리스트 : 
    모든 노드에 연결된 대한 정보를 차례대로 연결하여 저장한다.
    비교적 효율적
    속도가 조금 느리다.
'''

#인접리스트
print('인접리스트')
graph = [ [] for _ in range(3) ]
#행이 3개인 2차원 리스트로 인접리스트 표현하기

# 노드 0에 연결된 노드 정보 저장 (노드,거리)
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))
print(graph)
print()

# DFS
'''
Depth-First-Search / 깊이우선탐색
의미:
    그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
동작과정:
    1. 탐색 시작 노드를 스택에 삽입하고, 방문처리를 한다.
    2. 스택의 최상단 노드에 방문하지 않은 인접노드가 있으면,
        인접노드를 스택에 넣고 방문처리
        방문하지않은 인접노드가 없으면, 스택에서 최상단 노드를 꺼낸다.
    3. 1~2를 반복
    노드의 탐색순서는, 스택에 들어간 순서이다.

시간 복잡도 :
    데이터 개수가 N개인 경우
    O(n)
    시간이 걸린다.
구현:
    스택
'''

# 각 노드가 연결된 정보를 2차원 리스트 자료형으로 표현했다. 
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

def dfs(graph, v, visited):
    # 노드를 방문처리
    
    visited[v] = True
    print(v, end= ' ')
    #현재
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

print('DFS 깊이우선 탐색')
dfs(graph, 1, visited)



# BFS
'''
Breadth First Search 알고리즘  / 너비 우선 탐색
의미:
    가까운 노드부터 탐색하는 알고리즘이다.
    큐를 사용하는 것이 좋다. (선입선출)
동작과정 :
    1. 탐색 시작 노드를큐에 삽입하고 방문 처리를 한다.
    2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
    3. 1~2를 반복해서 수행
구현:
    deque 라이브러리를 사용하는 것이 좋다.
시간복잡도:
    O(n) 의 시간이 소요된다.
    일반적으로 DFS보다 소요시간이 좋은편.
'''

visited = [False] * 9

from collections import deque #deque 라이브러리 사용

def bfs(graph, start, visited):
    queue = deque([start])
    #현재의 노드를 방문했다고 한다.
    visited[start] = True

    # 이것을 큐가 빌 때 까지 반복한다.
    while queue:
        #큐에서 하나의 원소를 뽑아서 출력한다.
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

print()
print('BFS 넓이 우선 탐색 ')
bfs(graph, 1 ,visited)