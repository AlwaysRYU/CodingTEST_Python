# JadenCase
# https://programmers.co.kr/learn/courses/30/lessons/12951

import re

def solution(s):
    answer = '' 
    small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    
    if s[0] in small :
        answer += big[small.index(s[0])]
    # elif s[0] == " ":
    #     answer += ""
    else :
        answer += s[0]

    for i in range(1,len(s)):
        if s[i-1] == " " and s[i] in small:
            answer += big[small.index(s[i])]
        elif s[i] in small:
            answer += s[i]
        elif s[i] in big :
            if s[i-1] == " " : answer += s[i]
            else : answer += small[big.index(s[i])]
        else:
            answer += s[i]
    return answer

# 코멘트 :
'''
정규식으로 풀어보려고 했는데, 그 대문자로 바꾸는 방법을 몰라서 쓰지 못했다.
공백 간격으로 분리해서 ,a-z 면 맨앞글자를 대문자로 바꿔주는것.
이게더 어려웠을 지도 모르겠다.
'''

print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution(" abc"))
print(solution("123123abd dffdGdfGDF"))
print(solution(" A a b c d e"))
'''
=
    # p = re.compile('[a-z]')
    # if p.match(s[0]):
    #     print('Match found: ', m.group())
    # else:
    #     print('No match')
'''