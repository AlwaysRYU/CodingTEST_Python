# 시저암호
# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(Strr, N) :
    answer = ""
    somun = "abcdefghijklmnopqrstuvwxyz"
    damun = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
    for i in Strr :
        if i == " " :
            answer += " "
            continue
        elif i in somun :
            number = somun.find(i) + N
            answer += somun[number%26]
        else :
            number = damun.find(i) + N
            answer += damun[number%26]
    return answer

print(solution("AB",1 ))