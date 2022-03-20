test = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


def solution(places):
    answer = []
    "위 아래 우측 좌측 / 우측위/ 우측아래/ 좌측아래 / 좌측위"
    dx = [ -1, 1, 0, 0, -1, 1, 1, -1]
    dy = [ 0, 0, 1, -1, 1, 1, -1, -1]

    for i in range(5):
        print(str(i+1) + "번째 테이블 : " + str(places[i]))
        covid = 1
        # 시작
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    print(j,k)
                    # P면, 검증시작
                    if manjok(i,j,k,places,0) == 0 :
                        # 안지키고 있으면
                        print(str(i+1) + "번째 강의실은 방역을 안지킴")        
                        covid = 0
        
        answer.append(covid)
    return answer 

    
def manjok(i,a,b,places,level):
    
    "위 아래 우측 좌측 / 우측위/ 우측아래/ 좌측아래 / 좌측위"
    dx = [ -1, 1, 0, 0, -1, 1, 1, -1]
    dy = [ 0, 0, 1, -1, 1, 1, -1, -1]

    if level == 1 :
        count = 0
        for l in range(4):
            if a + dx[l] < 0 or a + dx[l] > 4 or b + dy[l] < 0 or b + dy[l] > 4 :
                continue
            if places[i][a + dx[l]][b + dy[l]] == "P" :
                count += 1
        if count >= 2: return 0
    # a b는 좌표
    else: 
        for l in range(4):
            if a + dx[l] < 0 or a + dx[l] > 4 or b + dy[l] < 0 or b + dy[l] > 4 :
                continue
            if places[i][a + dx[l]][b + dy[l]] == "P" :
                return 0
            elif places[i][a + dx[l]][b + dy[l]] == "O":
                if manjok(i, a+ dx[l],b + dy[l], places, 1) == 0 :
                    return 0

    print("방역지키고있음")
    return 1

print(solution(test))



def solution(places):
    answer = []
    "위 아래 우측 좌측 / 우측위/ 우측아래/ 좌측아래 / 좌측위"
    dx = [ -1, 1, 0, 0, -1, 1, 1, -1]
    dy = [ 0, 0, 1, -1, 1, 1, -1, -1]

    for i in range(5):
        covid = 1
        # 시작
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    # 검증시작
                    if manjok(i,j,k,places,0) == 0 :    
                        covid = 0
        
        answer.append(covid)
    return answer 

    
def manjok(i,a,b,places,level):
    dx = [ -1, 1, 0, 0, -1, 1, 1, -1]
    dy = [ 0, 0, 1, -1, 1, 1, -1, -1]

    if level == 1 :
        count = 0
        for l in range(4):
            if a + dx[l] < 0 or a + dx[l] > 4 or b + dy[l] < 0 or b + dy[l] > 4 :
                continue
            if places[i][a + dx[l]][b + dy[l]] == "P" :
                count += 1
        if count >= 2: return 0
    # a b는 좌표
    else: 
        for l in range(4):
            if a + dx[l] < 0 or a + dx[l] > 4 or b + dy[l] < 0 or b + dy[l] > 4 :
                continue
            if places[i][a + dx[l]][b + dy[l]] == "P" :
                return 0
            elif places[i][a + dx[l]][b + dy[l]] == "O":
                if manjok(i, a+ dx[l],b + dy[l], places, 1) == 0 :
                    return 0
    return 1