# 삼각달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3


def solution(n):
    answer = []
    for i in range(n):
        answer.append([0] * (i + 1))
    print(answer)
    
    # 넣는 수
    number = 1 
    maxnum = 0
    temp = 1
    while temp <= n:
        maxnum += temp
        temp += 1
    print( "N : " + str(n))
    print("한계 : " + str(maxnum))
    NN = 1 # 번째
    while True :
        if NN > n : break
        di = NN // 3
        print("몫(di)은 : " + str(di) + "   지금순서는 : " + str(NN))
        if (NN % 3) == 1 :
            # 1, 4, 7, 10 번째
            for i in range(n - (NN-1)):
                if answer[0 + (2*di) + i][0+di] == 0:
                    answer[0 + 2*di + i][0+di] = number
                    number += 1
            NN += 1
            print(answer)
            continue
        elif (NN % 3) == 2:
            # 2, 5, 8, 11 번째
            for i in range(n - (NN-1)):
                if answer[-1-di][ 1 + (di) + i] == 0:
                    answer[-1-di][1+(di)+i] = number
                    number += 1
            print(answer)
            NN += 1
            continue
        elif (NN % 3) == 0:
            # 3, 6, 9, 12 번째..
            for i in range(n - (NN-1)):
                if answer[-2 -(di-1) -i ][-1-(di-1)] == 0:
                    answer[-2 -(di-1) -i ][-1-(di-1)] = number
                    number += 1
            print(answer)
            NN += 1
            continue
    real = []
    for i in range(len(answer)):
        real += answer[i]
    return real

n1, n2, n3 = 4,5,6

# print(solution(7))
# print(solution(n1))
# print(solution(n2))
# print(solution(n3))


# 다른사람의 풀이
def solution2(n):
    dy=[1,0,-1]
    dx=[0,1,-1]

    b=[[0] * i for i in range(1,n+1)]
    print(b)

    x,y=0,0
    num=1
    d=0
    
    while num <= (n+1) * n // 2:
        b[y][x]=num
        ny=y+dy[d]
        nx=x+dx[d]
        num+=1
        if 0 <= ny < n and 0<=nx<=ny and b[ny][nx]==0:y,x=ny,nx
        else:d=(d+1)%3;y+=dy[d];x+=dx[d]
    
    return sum(b,[])
# 고뇌의 흔적
print(solution2(6))
'''
def solution(n):
    answer = []
    for i in range(n):
        answer.append([0] * (i + 1))
    print(answer)
    
    # 넣는 수
    number = 1 
    maxnum = 0
    temp = 1
    while temp <= n:
        maxnum += temp
        temp += 1

    print(maxnum)
    NN = 1 # 번째
    while True :
        di = NN // 3
        print("몫(di)은 : " + str(di) + "   지금순서는 : " + str(NN))
        if (NN % 3) == 1 :
            # 1, 4, 7, 10 번째
            for i in range(n - (NN-1)):
                if answer[0 + (2*di) + i][0+di] == 0:
                    answer[0 + 2*di + i][0+di] = number
                    number += 1
                    if number > maxnum : break
            NN += 1
            print(answer)
            continue
    
        elif (NN % 3) == 2:
            # 2, 5, 8, 11 번째
            for i in range(n - (NN-1)):
                if answer[-1-di][i] == 0:
                    answer[-1-di][i] = number
                    number += 1
                    if number > maxnum : break
            NN += 1
            continue
        elif (NN % 3) == 0:
            # 3, 6, 9, 12 번째..
            for i in range(n):
                if n-1-i <= 0 : continue
                if answer[n-1-i][-1-(di-1)] == 0:
                    answer[n-1-i][-1-(di-1)] = number
                    number += 1
                    if number > maxnum : break
            NN += 1
            continue
    return answer
'''