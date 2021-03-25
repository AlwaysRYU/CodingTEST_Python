# 두 개 뽑아서 더하기 
'''
https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3
난이도 : Level 1
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''
#내가 푼것
numbers = [ 2, 1, 3, 4, 1]

def solution(numbers):
    answer = []
    a = len(numbers)
    
    for i in range(a) :
        temp1 = numbers[i]

        #마지막일 경우는 탈출
        if i == a-1 : break 

        for j in range(i+1,a):
            temp2 = numbers[j]
            temp3 = temp1 + temp2
            #값이 없을 경우 answer에 추가한다.
            if temp3 not in answer :
                answer.append(temp3)
    
    answer.sort()
    return answer

#3 더 간단한 풀이
def solution2(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

#리스트중복제거 메소드 set를 사용함으로써 더욱 간단하게 풀이할 수 있다.


print(solution(numbers))