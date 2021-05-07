# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

rec = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    
    # method = { "Enter" : "님이 들어왔습니다.", "Leave" : "님이 나갔습니다."}
    data = {}
    

    for i in range(len(record)):
        temp = record[i].split(" ")
        print(temp)
        if temp[0] == "Enter" :
            data[temp[1]] = temp[2]
        elif temp[0] == "Leave" :
            continue
        elif temp[0] == "Change" :
            data[temp[1]] = temp[2]

    for i in range(len(record)):
        temp = record[i].split(" ")
        print(temp)
        if temp[0] == "Enter" :
            answer.append(str(data[temp[1]] + "님이 들어왔습니다."))
        elif temp[0] == "Leave" :
            answer.append(str(data[temp[1]] + "님이 나갔습니다."))
        elif temp[0] == "Change" :
            continue
    return answer 

print(solution(rec))


#다른 사람의 풀이
def solution2(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

#개인적으로 내것이 더좋은것 같다.