# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    L = len(s)
    Number = answer // 2
    print(Number)
    count = 0
    for i in range(1,Number) :
        temp = ""
        for j in range(i,L,i):
            print(s[j:j+i])

        # for j in range(0, L ,i) :
        #     if j == 0 :
        #         before = s[:i]
        #         count = 1
        #         continue

        #     jigum = s[ j : j + i]
        #     print(jigum)
        #     # if before == jigum :
        #     #     count += 1
        #     # else :
        #     #     temp += str(count) +
        #     #     before = jigum
        #     #     count = 1

        #     print(j)
            #



    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))