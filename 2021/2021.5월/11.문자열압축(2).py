# 문자열 압축 (2트)
# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3


t1 = "aabbaccc"
t2 = "ababcdcdababcdcd"
t3 = "abcabcdede"
t4 = "abcabcabcabcdededededede"
t5 = "xababcdcdababcdcd"

def solution(s):
    answer = 0
    temp = len(s) // 2
    leng = []

    
    for i in range(1,temp + 1):
        count = 1
        strr = s[0:i]
        
        result = ""
        for j in range(i,len(s),i):
            if s[j:j+i] == strr :
                count += 1
            else :
                if count == 1 :
                    count = ""
                result += str(count) + strr
                strr = s[j:j+i]
                count = 1

        if count == 1: count = ""
        result += str(count) + strr
        print(result)
        leng.append(len(result))
        leng.sort()

    return leng[0]

print(solution(t1))


 
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