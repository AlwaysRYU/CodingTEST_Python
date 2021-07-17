# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

# 방법 1
# 문제를 그대로 코드로 구현하는 방법
def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    while scoville :
        
        if scoville[0] >= K :
            return answer
        else :
            scoville.append(scoville[0] + (scoville[1] * 2))
            del scoville[0]
            del scoville[0]
            if len(scoville) == 1 :
                if (scoville[0]) < K :
                    return -1
            scoville.sort()
            answer += 1
    return -1

# print(solution([1, 2, 3, 9, 10, 12], 7))

# 테스트 케이스는 모두 통과하지만, 시간초과 오류가 있다.
# 원인은 매 번 정렬을 하는 것이 원인이라고 생각한다.
# 그렇다면, 매번 정렬을 안해도 되는 방법을 생각해보자.

# 그 방법은 힙이라고 생각했다.
import heapq
def solution2(arr, K):
    answer = 0

    heapq.heapify(arr)
    while arr :
        
        a = heapq.heappop(arr)
        if a >= K :
            return answer
        else :
            b = heapq.heappop(arr)
            heapq.heappush(arr, a + b*2) 
            if len(arr) == 1 :
                if (arr[0]) < K :
                    return -1
            answer += 1
    return answer
    
print(solution2([1, 2, 3, 9, 10, 12], 7))


# 다른 사람의 풀이
# 대부분 힙을 이용한다.