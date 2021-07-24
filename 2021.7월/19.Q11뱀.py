# 뱀
# https://www.acmicpc.net/problem/3190


N = int(input())
board = [[False] * N for _ in range(N) ]

apples = int(input())
for i in range(apples):
    y = input().split(" ")
    # 사과 위치
    board[y[0] -1][ y[1]-1 ] = True
 
snake = [0,0]
print(board)





