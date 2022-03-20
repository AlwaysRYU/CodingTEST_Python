# 이진 변환 반복하기
# https://programmers.co.kr/learn/courses/30/lessons/70129?language=python3

# 나의 풀이
def solution(s):
    answer = []
    totalnext = 0
    totalzero = 0
    while True:
        print("이번 문자 : " + s)
        if s == "1" :
            break
        tempstr = ""
        for i in s :
            if i == "1" :
                tempstr += "1"
            else :
                totalzero += 1
        totalnext += 1
        nextt = format(len(tempstr), 'b')
        print(nextt)
        s = str(nextt)
    answer.append(totalnext)
    answer.append(totalzero)
    return answer 


# 다른 사람의 풀이
def solution2(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        #count를 셈
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]

# count랑 bin을 사용했네.

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))

