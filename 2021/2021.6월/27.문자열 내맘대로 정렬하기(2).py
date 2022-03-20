# 문자열 내맘대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915

# 나의풀이
def begyo(Strr1, Strr2, n):
    if Strr1[n] == Strr2[n] :
        templist = sorted([Strr1, Strr2])
        return templist[0], templist[1]
    elif Strr1[n] < Strr2[n] :
        return Strr1, Strr2
    else:
        return Strr2, Strr1

def solution(string, n):
    number = len(string) -1

    for i in range(len(string)-1):
        for j in range(number) :
            string[j], string[j+1] = begyo(string[j], string[j+1],n)
        number -= 1
    return string

# 다른 사람의 풀이
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])
# lambda는 알고있었는데 같은것도 자동으로 정렬해주는 줄 몰랐다.
# lambda를 응용해보자.

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))