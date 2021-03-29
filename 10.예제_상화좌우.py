# 예제 4-1 상하좌우
'''
입력 
공간의 크기를 나타내는 N이 주어진다.
N은 n*n 배열이다.
1,1 부터 시작하여 
R - 우 L - 좌 U - 위 D - 밑
을 입력받아서 최종 위치를 출력한다.
이동할 공간이 없을땐 이동하지 않는다.
'''

#류기탁 풀이
N = int(input('배열 크기 : '))
moves = input().split()

x, y = 1, 1

for i in moves:
    if i == 'R' :
        if y == N : continue
        y += 1
    elif i == 'L' :
        if y == 1 : continue
        y -= 1
    elif i == 'U' :
        if x == 1 : continue
        x -= 1
    elif i == 'D' :
        if x == N : continue
        x += 1

print(x,y)

#책 풀이
move_types = ['L', 'R', 'U', 'D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for move in moves :
    for i in range(len(move_types)):
        if moves == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > N or ny > N :
            continue
        x,y = nx, ny
print(x,y)