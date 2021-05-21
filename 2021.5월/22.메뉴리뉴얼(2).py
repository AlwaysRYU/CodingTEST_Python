# 메뉴 리뉴얼
#  2021.05.21.
# https://programmers.co.kr/learn/courses/30/lessons/72411

# 내생각
'''
1. 사용된 알파뱃 각각 집합처리
2. course 숫자별로 조합하기
3. 조합해서 가장 많은 수만 answer에 넣기.
문제 : 조합이 오래걸릴것같은데...
일단 해봅시다
'''

o1, c1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]
o2, c2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],	[2,3,5]	
o3, c3 = ["XYZ", "XWY", "WXA"], [2,3,4]
# 순열 조합
import itertools

def solution(orders, course):
    answer = []
    for i in course :
        # 알파벳 집합 초기화
        alphabet = []
        for j in range(len(orders)):
            if len(orders[j]) >= i :
                # 문자열이 즉 시킨 요리가 코스수 보다 같고 ,클때만 해야함
                for k in range(len(orders[j])):
                    # 그 알파벳을를 넣는다
                    if not orders[j][k] in alphabet :
                        alphabet.append(orders[j][k])

        print(i)
        print("의 개수 이상인 알파벳")
        print(alphabet)
        print()
        templist = list(itertools.combinations(alphabet,i))
        print(templist)           
        
        for j in range(len())


        


    return answer


print(solution(o1,c1))
# print(solution(o2,c2))
# print(solution(o3,c3))