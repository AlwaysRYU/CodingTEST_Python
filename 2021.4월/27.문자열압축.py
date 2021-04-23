# 문자열 압축
# 2021.04.23.
# https://programmers.co.kr/learn/courses/30/lessons/60057
'''
문자열을 문자의 개수와 반복되는 값으로 표현하기.
압축한 문자열중 가장 짧은 것의 길이를 리턴하라.
'''
sss = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

def solution(s):
    answer = 0
    max = int(len(s)/2)

    # 자르는 수 
    Ss = 1
    before = ""
    anslist = []

    for i in range(1,max):
        print()
        print()
        print("i의 수, 글자 분할개수 : " + str(i))
        tempmunja = ""
        ansN = 1
        for j in range(1,len(s)) : 
            print("j의 수 : " + str(j))
            before = s[ (j-1)*i : j*i]
            print("----before : " + before)
            now = s[ j*i : (j+1)*i ]
            print("----now : " + now)

            if before == now :
                ansN +=1
            elif before != now :
                tempmunja += (str(ansN) + before)
                ansN = 1
            if (len(s) - i == j) : 
                tempmunja += (str(ansN) + before)
                break
        
        print(str(i) + "의 tempmunja : " + str(tempmunja))

    #이거 1제거해주기

    anslist.append(len(tempmunja))
    anslist.sort()
    answer = anslist[0]

    return answer

# print(solution(sss[0]))
# print(solution(sss[1]))
# print(solution(sss[2]))
# print(solution(sss[3]))
# print(solution(sss[4]))

# 다른사람의 풀이
def solution2(s):
    length = []
    result = ""
    
    #글자의 길이가 1이면 1출력
    if len(s) == 1:
        return 1
    
    # cut은 1부터 글자의 길이를 2로 나눈 몫에 1을 더한 수까지 
    # cut = 1,2,3,4,5
    for cut in range(1, len(s) // 2 + 1): 
        # 카운터
        print("cut : " + str(cut))
        count = 1

        # tempstr은 글자 처음부터 cut까지 
        tempStr = s[:cut] 

        #cut부터 컷마다, 끝까지
        for i in range(cut, len(s), cut):
            # 만약 같으면, 카운트
            # s[i:i+cut]은 다음것
            if s[i:i+cut] == tempStr:
                count += 1
            # 
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i+cut]
                count = 1
        
        # 1을 ' '으로 바굼
        if count == 1:
            count = ""

        result += str(count) + tempStr
        length.append(len(result))
        result = ""
        print(length)
    return min(length) # length에서 최소를 출력


print(solution2(sss[0]))
# print(solution2(sss[1]))
# print(solution2(sss[2]))
# print(solution2(sss[3]))
# print(solution2(sss[4]))