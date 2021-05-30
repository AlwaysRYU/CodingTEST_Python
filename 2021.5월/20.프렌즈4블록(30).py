# 프렌즈 4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679
# 2021.05.30.


m1, n1, b1 = 4,	5,	["CCBDE", "AAADE", "AAABF", "CCBBF"]
m2, n2, b2 = 6,	6,	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


# 다른사람의 풀이
def pop_num(b, m, n):
    # 집합 자료형
    pop_set = set() 
    # search
    for i in range(1, n):
        for j in range(1, m):
            # 만약 사각형이 모두 같으면
            if b[i][j] == b[i-1][j-1] == b[i-1][j] == b[i][j-1] != '_':
                # 집합에 
                pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
    # set_board
    for i, j in pop_set:
        b[i][j] = 0        
    for i, row in enumerate(b):
        empty = ['_'] * row.count(0)
        b[i] = empty + [block for block in row if block != 0]
    return len(pop_set)
     
def solution(m, n, board):
    count = 0
    b = list(map(list,zip(*board)))
    while True:
        pop = pop_num(b, m, n)
        if pop == 0: return count
        count += pop


'''
def find(x, y, board):
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    dl = [[0,1],[0,-1],[1,0],[-1,0]]
    count = 0
    m = len(board)
    print(m)
    n = len(board[0])
    print(n)
    zongbok = ["0" * n ] * m
    zongbok[x][y] = "1"
    print(zongbok)

    block = board[x][y]
    print(block)

    for i in range(4):
        if 0 <= (x + dl[i][0]) < m and 0 <= (y + dl[i][1]) < n and board[x + dl[i][0]][y + dl[i][1]] == block and zongbok[x + dl[i][0]][y + dl[i][1]] == "0":
            count += find(x+dl[i][0], y+dl[i][1], board)
    
    return count

def solution(m,n,board):
    answer = 0

    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i+1][j] == board[i+1][j+1] == board[i][j+1] :
                print(board[i][j])
                print(str(i) + " " + str(j))
                find2()


    # print(find(0,0, board))    


    return answer

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
'''