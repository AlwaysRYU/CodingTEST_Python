# 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930


def solution(s):
    answer = ''
    s = s.split(" ")
    print(s)
    for i in s :
        for j in range(len(i)) :
            if (j + 1) % 2 == 1 :
                answer += i[j].upper()
            else :
                answer += i[j].lower()
        answer += " "
    return answer[:-1]
print(solution("try hello world"))

# 다른사람의 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))