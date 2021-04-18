# 음료수 얼려먹기
# 2021.04.17. 
'''
N * M 크기의 얼음 틀이 있다.
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
얼음 틀 모양이 주어졌을 때, 생성되는 아이g스크림의 개수를 구하는 프로그램을 작성하라.

EX 
00110
00011
11111
00000

출력 : 3

'''



# N, M을 공백으로 구분하여 입력받기
print(" N M 을 입력하세요 : ")
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
def dfs(x,y) :
    # 만약 범위를 멋어난 다면 바로 종료한다.
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False

    # 현재 노드를 방문하지 않았다면,,,
    if graph[x][y] == 0 :
        # 1로 바꾸고
        graph[x][y] = 1
        # 상,하,좌,우 모두 재귀로 호출하면됨
        dfs(x -1 , y) # 좌측으로
        dfs(x, y-1) # 왼쪽으로
        dfs(x+1, y) # 우측으로
        dfs(x, y+1) #밑으로
        return True
    
    return False


result = 0

#일일히 전부 확인
for i in range(n):
    for j in range(m) :
        #현재위치에서 DFS 수행
        if dfs(i,j) == True :
            result += 1

print("결과 : ")
print(result)






