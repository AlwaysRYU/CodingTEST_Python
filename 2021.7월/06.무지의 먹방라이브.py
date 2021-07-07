# 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

# 그대로 했더니 시간 초과 났다.
def solution(times, k):
    eat = 0
    Number = len(times)
    while True :
        if eat == Number :
            eat = 0
        if times[eat] != 0 :
            if k == 0 : 
                if eat == Number :
                    return 1
                else : 
                    return eat + 1
            times[eat] -= 1
            eat += 1
            k -= 1
            continue
        else :
            eat += 1
            continue
    

print(solution([3,1,2], 5)) # 1
print(solution([4, 3, 5, 6, 2], 7)) # 3
print(solution([4,1,1,5] ,4)) # 1
print(solution([3,1,1,1,2,4,3],12)) # 6

def solution2(times, n) :
    Number = len(times)
    MINN = min(times)
    n -= MINN
    for i in range(Number):
        times[i] -= MINN

# 우선순위 큐 - 힙을 이용해야한다.
# 자세한건 514 페이지를 살펴보자.
            