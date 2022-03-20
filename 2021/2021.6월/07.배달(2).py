# 배달_2
# https://programmers.co.kr/learn/courses/30/lessons/12978?language=python3

N, R, K = 5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3
N2, R2, K2 = 6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],	4

from collections import deque

def solution(N, road, K):
    answer = 0
    nodes = {}
    dist = {i : float('inf') if i != 1 else 0 for i in range(1,N+1)}
    # minimal = { i : {} for i in range(1,N+1)}
    # print(minimal)
    for v1, v2, d in road:
        nodes[v1] = nodes.get(v1, []) + [(v2, d)]
        nodes[v2] = nodes.get(v2, []) + [(v1, d)]
    print(nodes)
    que = deque([1])
    print(que)
    while que:
        cur_node = que.popleft()
        for nxt_node, d in nodes[cur_node]:
            if dist[nxt_node] > dist[cur_node] + d:
                dist[nxt_node] = dist[cur_node] + d
                que.append(nxt_node)

    return len([True for dist in dist.values() if dist <= K])




    # for go, end, length in road :
        
   
    return answer

print(solution(N,R,K))