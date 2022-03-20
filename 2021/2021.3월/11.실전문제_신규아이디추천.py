# 신규아이디 추천
'''
https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
난이도 : 1
'''
'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''
new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):
    answer = ''
    #1단계 소문자로
    tempID = new_id.lower()
    answer = list(tempID)
    print('1단계')
    print(answer)

    #2단계 
    delete = 0
    available = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','-','_','.']
    for i in range(len(answer)):
        if answer[i] not in available :
            answer[i] = 'D'
            delete += 1
        if i == len(answer) - 1 : break
    
    for i in range(delete) :
        answer.remove('D')
    print('2단계')
    print(answer)
    
    #3단계 연속된 .제거 
    delete = 0
    temp = 0
    for i in range(len(answer)):
        if answer[i] == '.' :
            if temp >= 1 : 
                answer[i] = 'D'
                delete += 1
            else : 
                temp += 1
        else : temp = 0
        if i == len(answer) -1 : break

    for i in range(delete) :
        answer.remove('D')
    print('3단계')
    print(answer)

    #4단계 .맨뒤 맨앞제거
    delete = 0 
    while len(answer) >= 1 :
        if answer[0] == '.' :
            answer.remove('.')
        else : break

    while len(answer) >= 1: 
        if answer[len(answer)-1] == '.' :
            answer.pop()
        else : break

    print('4단계')
    print(answer)
    
    #5단계 빈문자열이라면 a대입
    if len(answer) == 0 : 
        answer.append('a') 

    #6단계 길이는 15 까지.
    while len(answer) >= 16 : 
        answer.pop()
        if answer[len(answer)-1] == '.' : answer.pop()

    print('6단계')
    print(answer)

    #7단계 
    if len(answer) <=2 : 
        temp = answer.pop()
        while len(answer) < 3 : 
            answer.append(temp)
        
    print('7단계')
    print(answer)
    dap = ''.join(answer)
    return dap

print(solution(new_id))


#다른사람의 풀이----------------------------------------
import re

def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
#정규식을 제거한 버전이래






