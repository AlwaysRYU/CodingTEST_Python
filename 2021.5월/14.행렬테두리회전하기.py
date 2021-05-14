# 행렬테두리 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3
# 
# 

a1, b1, c1 = 6,	6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
a2, b2, c2 = 3,	3,	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
a3, b3, c3 = 100,	97,	[[1,1,100,97]]

def solution(rows, columns, queries):
    answer = []
    base = []
    for i in range(rows):
        base.append([])
        for j in range(columns):
            base[i].append(i*columns + j + 1)
    print("처음 : ")
    print(base)
    print()

    for i in range(len(queries)):
        fx = queries[i][0] - 1
        fy = queries[i][1] - 1
        lx = queries[i][2] - 1
        ly = queries[i][3] - 1

        minnumber = 0

        lastnumber = base[fx + 1][fy]
        
        temp = 0

        # 북쪽, 우측으로
        base[fx][fy + 1 : ly + 1] = base[fx][fy:ly]

        # 동쪽 , 우측 밑으로
        # for j in range(last_x - first_x):
        #     # 마지막일 때
        #     if j == (last_x - first_x -1):
        #         base[first_x + 1][last_y] = temp
        #         temp = base[last_x][last_y]
            
        #     base[first_x + j + 2][last_y] = base[first_x + j + 1][last_y]

        # # 좌측으로
        # for j in range(last_y - first_y):
        #     if j == (last_y - first_y -1):
        #         base[last_x][last_y -1] = temp
        #         temp = base[last_x][first_y]
        #     base[last_x][last_y - j - 2] = base[last_x][last_y - j - 1]

        # # 마지막 위로
        # for j in range(last_x - first_x):
        #     if j == (last_y - first_y -1):
        #         base[last_x -1][first_y] = temp
        #         base[first_x][first_y] = lastnumber
        #         break

        #     base[last_x - j -2][first_y] = base[last_x - j-1][first_y]

        print(base)
        

    return answer


print(solution(a1,b1,c1))
# print(solution(a2,b2,c2))
# print(solution(a3,b3,c3))


#고뇌의 흔적
'''

def solution(rows, columns, queries):
    answer = []
    base = []
    for i in range(rows):
        base.append([])
        for j in range(columns):
            base[i].append(i*columns + j + 1)
    print(base)

    for i in range(len(queries)):
        first_x = queries[i][0] - 1
        first_y = queries[i][1] - 1
        last_x = queries[i][2] - 1
        last_y = queries[i][3] - 1
        
        change = []
        
        lastnumber = base[first_x + 1][first_y]
        temp = 0

        # 북쪽
        for j in range(last_y - first_y):
            if j == (last_y - first_y -1):
                temp = base[first_x][last_y]
            base[first_x][first_y + j + 1] = base[first_x][first_y +j]

        # 동쪽 , 우측 밑으로
        for j in range(last_x - first_x):
            # 마지막일 때
            if j == (last_x - first_x -1):
                base[first_x + 1][last_y] = temp
                temp = base[last_x][last_y]
            
            base[first_x + j + 2][last_y] = base[first_x + j + 1][last_y]

        # 좌측으로
        for j in range(last_y - first_y):
            if j == (last_y - first_y -1):
                base[last_x][last_y -1] = temp
                temp = base[last_x][first_y]
            base[last_x][last_y - j - 2] = base[last_x][last_y - j - 1]

        # 마지막 위로
        for j in range(last_x - first_x):
            if j == (last_y - first_y -1):
                base[last_x -1][first_y] = temp
                base[first_x][first_y] = lastnumber
                break

            base[last_x - j -2][first_y] = base[last_x - j-1][first_y]

        print(base)
'''