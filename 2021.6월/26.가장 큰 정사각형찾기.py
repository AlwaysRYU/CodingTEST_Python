# 가장 큰 정사각형 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3

def solution(board):
    answer = 0
    ri = [0,1]
    dia = [1,1]
    lef = [1,0]

    dx = [ 0, 1, 1 ]
    dy = [ 1, 1, 0 ]

    maxx = 1

    def square(x,y,count) :
        hoak = [0,0,0]
        for i in range(3):
            if 0 > (x + dx[i]) or (x + dx[i]) >= len(board) or 0 > (y + dy[i]) or (y + dy[i]) >= len(board[0]) :
                continue
            if board[x+dx[i]][y+dy[i]] == 0  :
                # 만약 우측, 대각, 아래에 0이면 정사각형이 아님 현재 가장큰 답을 리턴
                hoak[i] = 1
                continue
            else:
                square(x+dx[i], y + dy[i], count + 1)

        if maxx >= count and sum(hoak) == 0:
            maxx = count + 1

    print(square(1,1,1))
    print(maxx)
    return answer
'''
재귀는 여기서 쓰는 것이 아닌 것 같다.
참신한 풀이방법을 봤다. 나중에 다시 해보자.
'''

# 다른 나의 풀이
def solution2(B) :
    maxx = 1
    allzero = True
    if sum(B[0]) != 0 :
        allzero = False
    for i in range(1, len(B)):
        if sum(B[i]) != 0 :
            allzero = False
        for j in range(1, len(B[0])):
            if B[i][j] == 0 :
                continue
            if B[i-1][j-1] != 0 and B[i][j-1] != 0 and B[i-1][j] != 0 :
                B[i][j] = min(B[i-1][j-1], B[i][j-1], B[i-1][j]) + 1
                if maxx < B[i][j] :
                    maxx =B[i][j]
    if allzero == True :
        return 0
    return maxx * maxx
# 한케이스가 틀린다.
# 모든 요소가 0인 경우.
# 이렇게 리스트 형태를 바꾸는 방법은 기억해 두도록 하자.

print(solution2([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) #9
print(solution2([[0,0,1,1],[1,1,1,1]])) #4
print(solution2([[1,0],[0,0]]))
