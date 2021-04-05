# 모의고사
'''
https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
level : 1

수포자는 수학문제를 다음과 깉이찍는다.
1번 1 2 3 4 5 1 2 3 4 5... (1 2 3 4 5 반복)
2번 2 1 2 3 2 4 2 5 2 (2와 n) 1 3 4 5
3번 3 3 1 1 2 2 4 4 5 5  ( 3 1 2 4 5 ) 이렇게 2번 반복

가장 많은 문제를 맞힌 사람을 리턴함
예시 입 출력
1 2 3 4 5 -> 1
1 3 2 4 2 -> 1 2 3

'''

input1 = [1,2,3,4,5]
input2 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
input3 = [3, 3, 1, 1, 1, 1, 2, 3, 4, 5] 

def solution(answers):
    answer = []
    temp1 = 0
    temp2 = 0
    temp3 = 0
    
    j = 0
    #1 번확인
    for i in range(len(answers)) :
        j += 1
        if j == 6 : 
            j = 1
        if j == answers[i] :
            # 일치할 경우
            temp1 += 1
    print('1번학생이 답을 맞춘 횟수 ' + str(temp1) )
            
    
    # 2번 참가자 확인
    jj = 0
    jjj = [1,3,4,5]
    for i in range(len(answers)) : 
        if (i+1) % 2 == 1 : #홀수일 경우는 2로 고정
           j = 2
        else : 
            j = jjj[jj]
            jj += 1
            if jj == 4 : jj = 0
            

        if j == answers[i] :
            # 일치할 경우
            temp2 += 1

    print('2번학생이 답을 맞춘 횟수 ' + str(temp2) )
        
    # 3번 참가자 확인
    k, aaa = [3,1,2,4,5] , 0
    for i in range(len(answers)) : 

        if k[aaa] == answers[i] :
            temp3 += 1

        if (i+1) % 2 == 0 : #짝수일 경우는 업
            aaa += 1
            if aaa == 5 : aaa = 0
        
    print('3번학생이 답을 맞춘 횟수 ' + str(temp3) )
    
    tempans = []
    tempans.append(temp1)
    tempans.append(temp2)
    tempans.append(temp3)
    
    buzz = tempans[0]
    print(tempans)
    
    for i in range(len(tempans)):
        if buzz < tempans[i]:
            buzz = tempans[i]
    #최대값은 buzz
            

    for i in range(len(tempans)):
        if buzz == tempans[i]:
            answer.append(i+1)

    print(answer)
    return answer

print(solution(input1))
print(solution(input2))
print(solution(input3))