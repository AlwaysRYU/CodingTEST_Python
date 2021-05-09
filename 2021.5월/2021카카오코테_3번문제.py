'''
"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
'''
ex1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	
ex2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

def solution(n, k, cmd):
    answer = ''
    before = [ str(i) + "번째 캐릭터" for i in range(n)]
    now = k
    print(before)
    print("현재 위치 : " + str(before[now]))

    tempnumber = []
    tempvalue = []
    direct = []

    for i in range(len(cmd)):
        if cmd[i][0] == "U":
            print("위로")
            iss = cmd[i].split(" ")
            now = now - int(iss[1])
            if now < 0 : now = 0
            elif now >= len(before) : now = len(before)-1
            print("현재 위치 : " + str(before[now]))
        
        elif cmd[i][0] == "D":
            iss = cmd[i].split(" ")
            now = now + int(iss[1])
            if now < 0 : now = 0
            elif now >= len(before) : now = len(before)-1
            print("아래로" + str(iss[1]))
            print("현재 위치 : " + str(before[now]))

        elif cmd[i][0] == "C":
            print("삭제")
            tempnumber.append(now)
            tempvalue.append(before[now])
            direct.append(before[now+1])

            del before[now]
            if now < 0 : now = 0
            elif now >= len(before) : now = len(before)-1
            print("현재 위치 : " + str(before[now]))
        
        elif cmd[i][0] == "Z":
            print("복구")
            #insert(a,b) a위치에 b를 삽입
            for j in range(len(before)):
                if before[j+1] == direct[-1]:
                    before.insert(j,tempvalue[-1])
                    del tempvalue[-1]
                    del direct[-1]
                if j <= now:
                    now += 1
                    if now >= len(before) : now = len(before) -1
            print("현재 위치 : " + str(before[now]))
    print("연산후 테이블 : " + str(before))

    realbefore = [ str(i) + "번째 캐릭터" for i in range(n)]
    # j = 0
    # for i in range(len(realbefore)):
    #     if j >= len(before):
    #         answer += "X"
    #         continue 
    #     if realbefore[i] == before[j]:
    #         #같으면
    #         answer += "O"
    #         j += 1
    #     else:
    #         answer += "X"
        
    while realbefore :
        if realbefore[0] == before[0]:
            answer += "O"
            del realbefore[0]
            del before[0]
        else :
            answer += "X"
            del realbefore[0]
    return answer

# print(solution(8,2,ex1))
# print(solution(8,2,ex2))




def solution2(n, k, cmd):
    answer = ''
    belist = [ i for i in range(n)]
    print(belist)
    now = k
    print("현재 위치 : " + str(belist[now]))

    tempnumber = []

    for i in range(len(cmd)):
        if cmd[i][0] == "U":
            print("위로")
            iss = cmd[i].split(" ")
            now = now - int(iss[1])
            if now < 0 : now = 0
            elif now >= len(belist) : now = len(belist)-1
            print("현재 위치 : " + str(belist[now]))
        
        elif cmd[i][0] == "D":
            iss = cmd[i].split(" ")
            now = now + int(iss[1])
            if now < 0 : now = 0
            elif now >= len(belist) : now = len(belist)-1
            print("아래로" + str(iss[1]))
            print("현재 위치 : " + str(belist[now]))

        elif cmd[i][0] == "C":
            belist[now] = -1
            tempnumber.append(now)
            now += 1
            if now >= len(belist) : now = len(belist)-1
            print()
            print("현재 위치 : " + str(belist[now]))

        
        elif cmd[i][0] == "Z":
            print("복구")
            belist.insert(tempnumber[-1],tempnumber[-1])
            del tempnumber[-1]
            if tempnumber[-1] <= now :
                now += 1
                if now >= len(belist) : now = len(belist)-1
            print("현재 위치 : " + str(belist[now]))

    print("연산후 테이블 : " + str(belist))

    realbefore = [ i for i in range(n)]

    while realbefore :
        if realbefore[0] == belist[0]:
            answer += "O"
            del realbefore[0]
            del belist[0]
        else :
            answer += "X"
            del realbefore[0]
    return answer

    
print(solution(8,2,ex1))
print(solution(8,2,ex2))


