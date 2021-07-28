# 치킨배달 
# https://www.acmicpc.net/problem/15686

# COPYCODE
from itertools import combinations 

# 입력받기
N, M = map(int, input().split())
dak, house = [], []  # 치킨-1 집-2

for r in range(N):
    data = list(map(int, input().split()))
    # 여기서 치킨집과 집이 있다면 치킨집, 집목록에 넣어준다.
    for c in range(N) :
        if data[c] == 1:
            house.append((r,c)) # 집
        elif data[c] == 2:
            dak.append((r,c)) # 치킨집 

nCr = list(combinations(dak,M))

def chick_SUM(C) :
    result = 0
    # 모든집에 대해
    for hx, hy in house :
        # 가장 가까운 치킨집을 찾는다.
        temp = 1e9 # 최댓값, 무한대 처리임
        for cx,cy in nCr:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
            #가장 가까운 치킨집 까지의 거리를 더하기
        result += temp
    # 치킨거리의 합 반환
    return result

result = 1e9 #한무
for C in nCr :
    result = min(result, get_SUM(C)

print(result)