# 큰수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

# 그리디 문제
# 최선의 선택이 후에 결과에 영향을 주지않음
# 참신한 아이디어가 필요함.

def solution(number, k):
    answer = ''
    templist = list(number)
    answerlist = templist.copy()

    templist.sort()
    # before = templist[ : int(len(templist)/2) ]
    # after = templist[ int(len(templist)/2) : ]

    print(templist)
    print("현재 answerlist : " + str(answerlist))
    print(before)
    print(after)

    count = 0
    for i in range(len(answerlist)) :
        if count == k :
            continue
        if answerlist[i] in before :
            answerlist[i] = ""
            count += 1
        #count가 k와 같으면 탈출.
    answer = "".join(answerlist)
    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))

strr = "12345"

# 스택을 이용해서 풀어아야한다.

print(strr)