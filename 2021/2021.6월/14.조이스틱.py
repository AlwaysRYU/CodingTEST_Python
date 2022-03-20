# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860


# 1차 제출
def solution(name):
    alpha = [
        'A','B','C','D','E',
        'F','G','H','I','J',
        'K','L','M','N','O',
        'P','Q','R','S','T',
        'U','V','W','X','Y','Z'] #총 알파벳 개수 26게

    # 1. 먼저 각각의 상하 운동 수
    tempans = []
    totalupdown = 0
    for i in name :
        updown = alpha.index(i)
        if updown > 13 :
            updown = 26 - updown
        totalupdown += updown
        tempans.append(updown)
    print(tempans)
    # print(alpha[20])
    # print(alpha.index("Z"))
    # print(alpha.index("N") - alpha.index("A")) # 좌우 개수
    
    # 2. 좌
    left = 0
    leftlist = tempans.copy()
    leftlist[0] = 0
    for i in range(len(leftlist)-1, -1, -1) :
        leftlist[i] = 0
        left += 1
        if sum(leftlist) == 0 :
            break
        
    # 3. 우
    right = 0
    rightlist = tempans.copy()
    rightlist[0] = 0
    for i in range(1, len(leftlist)) :
        rightlist[i] = 0
        right += 1
        if sum(leftlist) == 0 :
            break

    if left >= right :
        return left + totalupdown
    else :
        return right + totalupdown

print(solution("JEROEN"))
print(solution("JAN"))

# 테스트 케이스 하나 틀린다.
# "ABAAAAAAAAABB" 의 경우를 생각해보자.
# 이경우 좌 우를 바꿔서 가야한다.

# 두번째, 정답 
def solution2(name):
    alpha = [
        'A','B','C','D','E',
        'F','G','H','I','J',
        'K','L','M','N','O',
        'P','Q','R','S','T',
        'U','V','W','X','Y','Z'] #총 알파벳 개수 26게

    # 1. 상하 이동 수를 구한다.
    tempans = []
    totalupdown = 0
    for i in name :
        updown = alpha.index(i)
        if updown > 13 :
            updown = 26 - updown
        totalupdown += updown
        tempans.append(updown)
    
    # 2.좌우 이동수를 구한다.
    array = tempans.copy()
    array[0] = 0 
    index = 0
    totalLR = 0
    a= 1
    while sum(array) != 0 :
        if array[index + a] != 0 and array[index - a] == 0 :
            #우측으로
            totalLR += a
            index = index + a
            array[index] = 0
            a = 1
        elif array[index + a] == 0 and array[index - a ] != 0 :
            # 좌측으로
            totalLR += a
            index = index - a
            array[index] = 0
            a = 1
        elif array[index + a ] == 0 and array[index - a] == 0 :
            a += 1
        elif array[index + a ] != 0 and array[index - a] != 0 :
            # 둘다 0이 아님 그러면 우측으로 
            totalLR += a
            index = index + a
            array[index] = 0
            a = 1

    # 3. 두개의 합을 출력한다.
    return totalLR + totalupdown

# 다른사람의 풀이 비슷하거나
# 내가 쫌 쉽게 푼것 같은데,, 히히

    
print(solution2("JEROEN"))
print(solution2("JAN"))


