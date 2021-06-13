
# 1. 문자열 내 p 와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    PC, YC = 0, 0
    for i in s :
        if i == 'p' or i == 'P' :
            PC += 1
        elif i == 'Y' or i == 'y' :
            YC += 1
    if PC != YC :
        return False
    return True


# 2. 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution2(s):
    answer = ''
    alpha = [
        'A','B','C','D','E',
        'F','G','H','I','J',
        'K','L','M','N','O',
        'P','Q','R','S','T',
        'U','V','W','X','Y','Z']
    
    templist = []
    biglist = []
    for i in s :
        if i in alpha :
            biglist.append(i)
        else:
            templist.append(i)
    templist.sort(reverse=True)
    for i in templist :
        answer += str(i)
    biglist.sort(reverse=True)
    for i in biglist :
        answer += str(i)
    return answer

print(solution2("Zbcdefg"))

#다른사람의풀이
def solution2_P(s):
    return ''.join(sorted(s, reverse=True))
print(sorted("fdjgkadklfl", reverse=True))
#문자열을 정렬하는 법이다.


# 3. 서울에서 김서방 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12919
def solution3(seoul):
    return "김서방은 " + str(seoul.index("Kim")) + "에 있다"

# 4. 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918

import re

def solution4(s):
    J = re.compile('[a-zA-Z]')
    print(len(s))
    if len(s) != 4 and len(s) != 6 :
        return False  
    for i in s :
        if J.match(i) :
            return False
    return True

print(solution4("1234"))
# 다른사람의 풀이
def solution4_P(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))
# 정규화를 제대로 사용하는 사람.


# 5. 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921
def solution5(n):
    if n == 1 :
        return 0
    elif n == 2 :
        return 1 
    elif n == 3 :
        return 2 
    answer = 2
    sosu = [2,3]
    for i in range(4 , n+1) :
        if (i % 2) == 0 or (i % 3) == 0 :
            continue
        for j in sosu :
            if (i % j) == 0 :
                continue
        
        sosu.append(i)
        answer += 1
    return answer

print(solution5(5))


# 6. 수박수박수박수박수?
# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution6(n):
    answer = ''
    for i in range(1,n+1):
        if (i%2) == 1 :
            answer += '수'
        else :
            answer += '박'
    return answer