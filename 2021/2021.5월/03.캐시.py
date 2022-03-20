# 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3


s1, c1 = 3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
s2, c2 = 3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
s3, c3 = 2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
s4, c4 = 5,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
s5, c5 = 2,	["Jeju", "Pangyo", "NewYork", "newyork"]
s6, c6 = 0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	

# 류기탁의 풀이
def solution(cacheSize, c):
    answer = 0
    page = []
    cities = []
    
    if cacheSize == 0 : return len(c) * 5
    
    for i in range(len(c)):
        cities.append(c[i].upper())
    print(cities)

    for i in range(len(cities)):
        if not cities[i] in page:
            if len(page) < cacheSize :
                page.append(cities[i])
                answer += 5
            else :
                page.append(cities[i])
                del page[0]
                answer += 5
        elif cities[i] in page:
            page.remove(cities[i])
            page.append(cities[i])
            answer += 1
            
    return answer


print(solution(s1,c1))
print(solution(s2,c2))
# print(solution(s3,c3))
# print(solution(s4,c4))
# print(solution(s5,c5))
# print(solution(s6,c6))

# 다른 사람의 풀이
def solution2(cacheSize, cities):
    import collections
    # maxlen 은 최대 수 자동으로 없애줌
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time