# K번째 수 
'''
https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
level : 1

배열 array의 i 번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, K번째에 있는 수를 구하려 합니다.
'''

test = [1,5,2,6,3,7,4]
command = [[2,5,3],[4,4,1],[1,7,3]]

#류기탁 풀이
def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        #위와 같은 것엔 3번 반복 0 1 2
        start = commands[i][0] -1
        count = commands[i][1] - commands[i][0] + 1

        temp = []
        for j in range(start, len(array)):
            temp.append(array[j])
            if len(temp) == count : break
        print(temp)

        #정렬
        temp.sort()
        answer.append(temp[commands[i][2]-1])
    return answer

print(solution(test,command))

#다른 사람의 풀이
def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#오늘의 파이썬
'''

'''