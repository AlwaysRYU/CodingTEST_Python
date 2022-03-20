# 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909?language=python3


a1 = "()()"	
a2 = "(())()"
a3 = ")()("	
a4 = "(()("


def solution(s) :
    answer = True
    stacknum = 0
    for i in s :
        if i == "(":
            stacknum += 1
        elif i == ")" :
            stacknum -= 1
        if stacknum < 0 : return False

    if stacknum == 0 : 
        return True
    else :
        return False

print(solution(a1))
print(solution(a2))
print(solution(a3))
print(solution(a4))

# 다른 사람의 풀이
def is_pair(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0
# if를 뒤에 쓰는 법을 배우자.
