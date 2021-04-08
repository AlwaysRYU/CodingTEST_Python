# 체육복
# 2021.04.08 
'''
https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

번호는 체격순이다.
바로 앞번호의 학생이나,
뒷번호의 학생에게만 빌려줄 수 있다.
ex 4번학생은 3, 5 만 빌려줄 수 있다.
체육복을 적절히 빌려 많은사람이 수강할 수 있도록 한다.

N : 전체 학생의 수
lost : 체육복을 도난 당한 학생들의 번호가 담긴 배열
reverse : 여벌의 체육복을 가져온 학생들 
return : 체육수업을 들을 수 있는 학생의 최댓값

특이사항 : 
여벌 체육복을 가져왔더라도, 도난당했을 수 있다.
이때는 빌려줄 수 없다.

예시
n : 5
lost : [2, 4]
reverse : [1,3,5]
return -> 5
'''

test1n, test1lost, test1reverse = 5, [2,4], [1,3,5]
test2n, test2lost, test2reverse = 5, [2,4], [3]
test3n, test3lost, test3reverse = 3, [3], [1]
test4n, test4lost, test4reverse = 5, [1,2,3], [2,3,4]


#나의 풀이
def solution(n,lost, reverse):
    answer = 0
    answer_list = []
    
    for i in range(n):
        answer_list.append(i+1)
    #체육복 리스트 생성

    print('생성 리스트')
    print(answer_list)

    for i in range(len(lost)):
        if lost[i] in reverse :
            #만약 잃어버린사람이 들고왔으면
            reverse.remove(lost[i])
            #빌려줄수 있는 명단에서 제거
            lost[i] = -10
            
        else :
            answer_list.remove(lost[i])
        
        #같은요소 제거     
    
    print('수강 리스트')
    print(answer_list)
    print('lost')
    print(lost)
    print('reverse')
    print(reverse)

    answer += len(answer_list)

    for i in range(len(lost)) :
        #잃어버린 학생에 대해
        temp = lost[i]        
        
        for j in range(len(reverse)):
            #만약 빌려줄 수 있으면 
            if (temp - 1) == reverse[j] :
                answer += 1
                reverse[j] = -5 #빌려줘서 쓸 수 없다.
                break
            elif temp == reverse[j] :
                answer += 1
                reverse[j] = -5
                break
            elif (temp + 1) == reverse[j] :
                answer += 1
                reverse[j] = -5
                break
    return answer

#다른 사람의 풀이
def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

print(solution(test1n,test1lost,test1reverse))
print(solution(test2n,test2lost,test2reverse))
print(solution(test3n,test3lost,test3reverse))
print(solution(test4n,test4lost,test4reverse))