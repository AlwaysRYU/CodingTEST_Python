# 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993

# 푸는 방법 고민
'''
정규표현식을 사용 하는 방법 : 
    예를들어 ABC가 들어오면, 
    []A[]B[]C[] 이거랑 매치가 되는지?
    '[A-Z]*C[A-Z]*B[A-Z]*D[A-Z]*' 이런식으로 했을때,
    D가 안들어가도 되는데, 정규식에선 반드시 사용해야한다.
    이걸 나눌 수 있을까.

'''

# 제출용 / 나의 풀이
def solution(skill, skill_trees):
    answer = 0
    for j in skill_trees:
        sk =True
        temp = 0
        for i in range(len(j)):
            if j[i] == skill[temp]:
                temp += 1
                if temp == len(skill) : 
                    break
            elif j[i] != skill[temp] and j[i] in skill :
                sk = False
                break
        if sk == True : answer += 1
    return answer


# 다른 사람의 풀이
def solution3(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_list = list(skill)
        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1
    return answer
# for else 에 대해 배웠다.

def solution2(skill, skill_trees):
    answer = 0
    for j in skill_trees:
        print()
        print(skill)
        print(j)
        sk =True
        temp = 0
        for i in range(len(j)):
            print("다음스킬 : " + str(skill[temp]))
            print("이번 스킬 글자 " + str(j[i]))
            if j[i] == skill[temp]:
                print("일치한다.")
                temp += 1
                if temp == len(skill) : 
                    break
            elif j[i] != skill[temp] and j[i] in skill :
                print(str(j) + "는 불가능하다.")
                sk = False
                break
        if sk == True : answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"] ))


'''
matchlist = ["[A-Z]*"]
    tempstr = "[A-Z]*"
    for i in range(len(skill)):
        tempstr += skill[i] + "[A-Z]*"
        matchlist.append(tempstr)
    print(tempstr)
    print(matchlist)
'''
