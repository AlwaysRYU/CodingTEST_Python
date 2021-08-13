# 경쟁적 전염
# https://www.acmicpc.net/problem/18405
from collections import deque
N, K = map(int, input().split())
array = []
# 리스트 입력 
VD = []


for i in range(N) :
    array.append(list(map(int, input().split())))

    for j in range(N) :
        # 바이러스가 존재할 경우
        if array[i][j] != 0:
            # 바이러스에 삽입
            VD.append((array[i][j],0,i,j))

S, X, Y = map(int, input().split())

print(array)
print(VD)
VD.sort() # 정렬_ 1부터해야함
q = deque(VD)


dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 너비 우선탐색 BFS
while q :
    Virus, ss, xx, yy = q.popleft()
    # S초가 지나거나 큐가 빌때까지 반복
    if ss == S:
        break
    
    for i in range(4):
        nx = xx + dx[i]
        ny = yy + dy[i]
        # 해당위치로 이동할 수 있는 경우 
        if 0 <= nx and nx < N and 0 <= ny and ny < N :
            # 아직 방문하지 않은 위치라면 그위치에 바이러스 넣기
            if array[nx][ny] == 0 :
                array[nx][ny] = Virus
                q.append((Virus, ss+1, nx,ny))
print(array)
print(array[X-1][Y-1])
