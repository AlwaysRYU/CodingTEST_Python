# 게임 개발
'''
게임 캐릭터가 맵안에서 움직이는 시스템을 개발한다.
캐릭터가 있는 장소는 N * M 크기의 직사각형.
각각의 칸은 육지 또는 바다이다.
캐릭터는 동서남북중 한 곳을 바라본다.
맥의 각 칸은 A, B로 나타낸다. A-> 북쪽으로부터 떨어진 칸의 개수. B-> 서쪽으로부터 떨어진 칸의 개수
캐릭터는 상하좌우로 움직일 수있다.
바다인 칸은 갈수 없다.
이동 메뉴얼은 다음과 같다.
1. 현재 위치에서 현재방향을 기준으로 왼쪽방향부터 차례대로 갈곳을정한다.
2. 왼쪽방향에 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸을 전진하다.
3. 왼쪽방향에 가보지 않은 칸이 없다면, 왼쪽방향으로 회전만 수행하고 1단계로 돌아간다.
4. 만약 모두 가본 칸이거나, 바다로 되어 있는 칸인 경우에는. 바라보는 방향을 유지하고 한칸 뒤로가고 1단계로돌아간다.
 단, 뒤쪽방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
위 과정을 반복적으로 수행하며, 캐릭터의 움직임에 이상이 있는지 테스트 하려고한다.
메뉴얼에 따라 캐릭터를 이동시킨 뒤에, 방문한 칸의 수를 출력하는 프로그램을 만드시오.
'''
'''
 n * m  의 공백을 구분하여 입력 한다.

0 북
1 동
2 남
3 서
0 육지, 1 바다
입력 예시
4 4         4*4맵생성
1 1 0       1,1에 북쪽을 보고 서있는 캐릭터
1 1 1 1     맵의 형태.
1 0 0 1 
1 1 0 1 
1 1 1 1 
출력 3
'''
#n, m을받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
'''
파이썬의 언더스코어 _
값을 무시하고 싶을 때 / 변수에 특별한 의미를 부여할대, 제화 함수로 사용할 때
'''
print('맵을 0으로 초기화')
print(d)


#캐릭터 좌표 위치 받기
x, y, direction = map(int, input().split())
d[x][y] = 1 #방문했다고 확인

#전체 맵
array = []
#전체 맵 입력
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서 0 1 2 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

#총 이동한수
count = 1
turn = 0

#왼쪽으로 회전하는 함수
def left():
    global direction
    direction -= 1
    if direction == -1 : direction = 3

while True:
    #처음 왼쪽으로 회전한다.
    left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn  = 0
        continue

    else:
        turn += 1
    
    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny

        else :
            break
        turn = 0
        
result = count
print(result)
