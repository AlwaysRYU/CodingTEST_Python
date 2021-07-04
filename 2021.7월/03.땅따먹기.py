# 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3
# 같은 열은 연속해서 할 수 없다.
# 이때 최대 점수를 출력 

# 초기 
# 단순하게 알고리즘을 그대로 구현,
def solution(land):
    answer = []
    for i in range(4):
        total = land[0][i]
        print(total)
        before = i
        for j in range(1, len(land)):
            templist = land[j].copy()
            templist[before] = -1
            print(templist)
            print("추가할 수 : " + str(max(templist)))
            total += max(templist)
            before = templist.index(max(templist))
            
        answer.append(total)
        print("최종 : " + str(total))
        print()
    return max(answer)

# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))
# 효율성 통과, 하지만 위와 같은 반례가 있다.
# 중복된 경우에는 다음 것까지 생각해서 해야 하는 것이다.


# 생각을 다시해보자. 충분히 풀수 있는 문제다.
