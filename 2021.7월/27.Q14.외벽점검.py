# 외벽점검
# https://programmers.co.kr/learn/courses/30/lessons/60062


    # 조건의 범위가 작다? -> 완전탐색 고려 

from itertools import permutations

def solution(n, weak, dist):
    answer = 0
    # 범위가 매우 작으므로 완전탐색 가능함.

    # 원형모양의 식당을 일자로 나열한다.
    length = len(weak)
    for i in range(length) :
        weak.append(weak[i] + n)
    print(weak)

    answer = len(dist) + 1 # 답이 나올수 없는 최대의 수
    
    # 0 부터 length -1 부터 시작하면 전부 돌릴수 있음
    for start in range(length) :
        # 사람을 나열하는 모든 경우의 수 각각에 대하여 확인 
        for worker in list(permutations(dist, len(dist))): 
            print(worker)
            count = 1 # 1부터 시작
            # 워커가 점검하는 마지막 위치임
            position = weak[start] + worker[count -1]

            for index in range(start, start + length) :
                
                if position < weak[index]:
                    count += 1
                    if count > len(dist) :
                        break
                    position = weak[index] + worker[count-1]
            answer = min(answer, count)
    if answer> len(dist) :
        return -1
    return answer

print(solution(12,	[1, 5, 6, 10],	[1, 2, 3, 4]))
print(solution(12,	[1, 3, 4, 9, 10],	[3, 5, 7]))