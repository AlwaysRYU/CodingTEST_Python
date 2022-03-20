# 연구소
# https://www.acmicpc.net/problem/14502

# 최대가 8 이므로 64칸중 3개의 벽을 맘대로 놓는 방법 64C3 해도 10만 정도가 넘지 않으므로, 전체탐색이 가능하다.
# 즉, 모두 검사하고, 그 검사할 때 마다 벽을 재는것이다.

n, m = map(int, input().split())
data = [] # 맵 -초기리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵리스트

for _ in range(n) :
    data.append(list(map(int,input().split())))

# 델타
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

# 깊이 우선 탐색
def virus(x,y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 
        if nx >= 0 and nx <n and ny >= 0 and ny < m :
            if temp[nx][ny] == 0 :
                temp[nx][ny] = 2
                virus(nx, ny)

# 안전 영역 계산
def get_score() :
    score  = 0
    for i in range(n):
        for j in range(m) :
            if temp[i][j] == 0 :
                score += 1
    return score

# 깊이우선 탐색 - 울타리 설치 이후 매번 안전영역의 크기를 계산
def dfs(count) :
    global result
    # 울타리가 3개설치된 경우
    if count == 3 :
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m) :
                if temp[i][j] == 2 :
                    virus(i,j) # 감염ㅁ시작

        # 안전영역의 최댓값 계산
        result = max(result, get_score)
        return
        
    for i in range(n) :
        for j in range(m) :
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)