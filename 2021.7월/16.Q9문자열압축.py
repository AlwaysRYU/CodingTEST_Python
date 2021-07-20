# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

# 최종 나의 풀이
def solution(s):
    answer = len(s)
    L = len(s)
    Number = answer // 2
    count = 0
    for i in range(1,Number+1) :
        temp = ""
        before = s[:i]
        for j in range( 0 , L , i ):
            jigum = s[j:j+i]

            if before == jigum :
                count += 1
            else :
                if count == 1 :
                    temp = temp + before
                elif count != 0 :
                    temp = temp + str(count) + before
                before = jigum
                count =1
        if count == 1 :
            temp = temp + before
        else :
            temp += str(count) + before
        if len(temp) < answer :
            answer = len(temp)
        count = 0
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("xxxxxxxxxxyyy"))

# 다른사람의 풀이
# 거의다 비슷하게 풀었다.
# 있는대로 알고리즘을 구현만 하면 되는 문제.