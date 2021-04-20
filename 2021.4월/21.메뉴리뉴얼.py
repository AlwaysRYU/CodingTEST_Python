# 메뉴 리뉴얼
# 2021 카카오 블라인드 코테
# 2021.04.20.
# https://programmers.co.kr/learn/courses/30/lessons/72411
'''
기존에는 단품으로만 제공하던 메뉴를 조합해
코스요리 혀태로 재구성해서 메뉴를 새로 구성하려한다.
이전에 각 손님들이 주문할 때 가장 많이 주문한 단품 메뉴들을 코스요리 메뉴로 구성하기로 했다.
단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려한다.

단품 메뉴들이 문자열 형식으로 담긴
orders

스카피가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 개수가 담긴 배열 course가 매개변수로 주어질때.
메뉴구성을 문자열형태로 담아서 return하도록
solution 함수를 완성하라.

단,
course배열은 2이상 10이하 자연수 / 오름차순 /중복없음
정답은 문자열형식으로 배열에 담아서 사전순으로 오름차순 정렬해라.
return


'''
oo = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
cc = [2,3,4]

# def solution(orders, course):
#     answer = []

#     # 총문자 종류 구하기
#     temp = []
#     for j in range(len(orders)):
#         temp += list(orders[j])
#     totalmunja = list(set(temp))
#     totalmunja.sort()
#     print(totalmunja)
    
#     # 코스의 수만큼 반복 예시1로는 3번
#     for i in range(len(course)):
#         # 이번 단계에서 메뉴 개수
#         Cnum = course[i]

#         #order의 수만큼 반복 예시1로는 6번
#         for j in range(len(orders)):
#             #한글자씩리스트로 변경
#             munjalist = list(orders[j])
#             print(munjalist)

#             for k in range(len(totalmunja)):
#     return answer

from itertools import combinations
from collections import Counter

#다른사람의 풀이
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)

print(solution(oo,cc))