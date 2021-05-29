# 방문길이
# https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3

# 제출용
def realsolution(dirs):
    answer = 0
    karo = [ [ 0 for i in range(10)] for j in range(11)]
    sero = [ [ 0 for i in range(11)] for j in range(10)]
    move = { 'U' : [-1, 0] , 'D' : [1,0], 'R' : [0,1], 'L' : [0,-1] }
    x, y = 5, 5

    for i in range(len(dirs)):
        nextx = x + move[dirs[i]][0]
        nexty = y + move[dirs[i]][1]
        
        if nextx < 0 or nextx > 10 or nexty < 0 or nexty > 10 :
            continue
        if dirs[i] == "L":
            if karo[x][y-1] == 0 :
                karo[x][y-1] = 1
                answer += 1
            
        elif dirs[i] == "R" :
            if karo[x][y] == 0 :
                karo[x][y] = 1
                answer += 1
        elif dirs[i] == "U"  :
            if sero[x-1][y] == 0:
                sero[x-1][y] = 1
                answer +=1
        elif dirs[i] == "D"  :
            if sero[x][y] == 0:
                sero[x][y] = 1
                answer +=1
        x = nextx
        y = nexty
    return answer


# 다른사람의 풀이
def solution3(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
#튜플 과 집합을 이용해서 중복을 제거한다.
# 이동한 칸수를 개수를 셌다.


def solutionx(dirs):
    answer = 0
    pyo = [ [ 0 for i in range(11)] for j  in range(11)]
    print(pyo)
    move = { 'U' : [-1, 0] , 'D' : [1,0], 'R' : [0,1], 'L' : [0,-1] }
    
    x, y = 5, 5
    pyo[x][y] = 1
    

    print("연산시작")
    beforezero = False
    for i in range(len(dirs)):
        print(dirs[i])
        print(move[dirs[i]])
        x += move[dirs[i]][0]
        y += move[dirs[i]][1]
        

        if x < 0 or x > 10 or y < 0 or y > 10 :
            continue

        if pyo[x][y] == 0 :
            print(str(x) + " " + str(y) + " : 여기는 안들렸습니다.")
            pyo[x][y] = 1
            answer += 1
            beforezero = True
        elif pyo[x][y] == 1 and beforezero == True:
            print(str(x) + " " + str(y) + " : 여기는 들렸지만, 전에 0이었습니다.")
            answer += 1
            beforezero = False
        else:
            beforezero = False


    print(pyo)

    return answer


def solution(dirs):
    answer = 0
    karo = [ [ 0 for i in range(10)] for j in range(11)]
    sero = [ [ 0 for i in range(11)] for j in range(10)]
    move = { 'U' : [-1, 0] , 'D' : [1,0], 'R' : [0,1], 'L' : [0,-1] }
    x, y = 5, 5

    for i in range(len(dirs)):
        print()
        print(dirs[i])
        print(move[dirs[i]])
        nextx = x + move[dirs[i]][0]
        nexty = y + move[dirs[i]][1]
        
        if nextx < 0 or nextx > 10 or nexty < 0 or nexty > 10 :
            continue

        print("현재 위치 : " + str(x) + str(y))
        print("다음 위치 : " + str(nextx) + str(nexty))

        if dirs[i] == "L":
            if karo[x][y-1] == 0 :
                karo[x][y-1] = 1
                answer += 1
            print(karo)
        elif dirs[i] == "R" :
            if karo[x][y] == 0 :
                karo[x][y] = 1
                answer += 1
            print(karo)
        elif dirs[i] == "U"  :
            if sero[x-1][y] == 0:
                sero[x-1][y] = 1
                answer +=1
            print(sero)
        elif dirs[i] == "D"  :
            if sero[x][y] == 0:
                sero[x][y] = 1
                answer +=1
            print(sero)
        
        x = nextx
        y = nexty
        print(answer)
    return answer 

di1, di2 = "ULURRDLLU", "LULLLLLLU"


# print(solution(di1))
# print(solution(di2))
print(solution("UDU"))
