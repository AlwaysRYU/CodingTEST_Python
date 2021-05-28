# 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412

i, q = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    
    resume = []
    for i in range(len(info)):
        resume.append(list(info[i].split(" ")))
    quest = []
    for i in range(len(query)):
        quest.append(list(query[i].split(" and ")))
    print(resume)
    print(quest)

    for i in range(len(quest)):
        tempanswer = 0
        food, score = quest[i][3].split(" ")
        print()
        print(str(i+1) + "번째 질문 : ")
        for k in range(len(resume)):
            print(quest[i][0])
            if quest[i][0] != "-" and quest[i][0] != resume[k][0]:
                continue
            print(quest[i][1])
            if quest[i][1] != "-" and quest[i][1] != resume[k][1]:
                continue
            print(quest[i][2])
            if quest[i][2] != "-" and quest[i][2] != resume[k][2]:
                continue
            print(food)
            if food != "-" and food != resume[k][3]:
                continue
            print(score)
            print(resume[k][4])
            if int(score) > int(resume[k][4]):
                print("여기는하나?")
                continue
            print(str(k + 1) + " 번째 지원자는 통과함")
            tempanswer += 1

        answer.append(tempanswer)
    return answer


# 위와 같은 코드는, 정답은 맞지만 효율성에서 탈락이다
# 반복문을 최대한 줄여보자.
def solution2(info, query):
    answer = [] 
    for i in query :
        Q = list(str(i).split(" "))
        print(Q)
        # 질문 준비 완료
        tempanswer = 0
        for k in info :
            lang, job, history, soul, test = str(k).split(" ")
            if Q[0] != "-" and Q[0] != lang:
                continue
            if Q[2] != "-" and Q[2] != job:
                continue
            if Q[4] != "-" and Q[4] != history:
                continue
            if Q[6] != "-" and Q[6] != soul:
                continue
            if int(Q[7]) > int(test):
                continue
            tempanswer += 1
        answer.append(tempanswer)
    return answer

print(solution2(i,q))
    

def solution3(info, query):
    answer = [] 
    for i in query :
        Q = list(str(i).split(" "))
        # 질문 준비 완료
        tempanswer = 0
        for k in info :
            lang, job, history, soul, test = str(k).split(" ")
            if Q[0] == "-" or Q[0] == lang:
                if Q[2] == "-" or Q[2] == job:
                    if Q[4] == "-" or Q[4] == history:
                        if Q[6] == "-" or Q[6] == soul:
                            if int(Q[7]) <= int(test):
                                tempanswer += 1
        answer.append(tempanswer)
    return answer

#시간초과 
# 줄이는 방법 :
# 1. -라면 굳이 안비교해도됨 -> 이미했다. 
# 2. 한번의 반복문으로 할 수 있나?
# 한 질문으로 모든 사람을 전수조사해야할 텐데
# 생각치못한방법이 있나.
# 2. split(" ")이 너무 시간을 끄나?