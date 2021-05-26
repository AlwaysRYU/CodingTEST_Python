# JadenCase
# https://programmers.co.kr/learn/courses/30/lessons/12951

import re

def solution(s):
    answer = ''
    # p = re.compile('[a-z]')
    # if p.match(s[0]):
    #     print('Match found: ', m.group())
    # else:
    #     print('No match')

        
    small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    
    if s[0] in small :
        answer += big[small.index(s[0])]
    elif s[0] == " ":
        answer += ""
    else :
        answer += s[0]

    for i in range(1,len(s)):
        if s[i-1] == " " and s[i] in small:
            answer += big[small.index(s[i])]
        elif s[i] in small:
            answer += s[i]
        elif s[i] in big :
            answer += small[big.index(s[i])]
        else:
            answer += s[i]
    
    if answer[-1] == " " :
        answer[-1] = ""
    return answer


print(solution("3people unFollowed me"))
print(solution("for the last week"))