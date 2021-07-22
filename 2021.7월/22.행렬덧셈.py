# 행렬덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950

#해결 - 나의 풀이
def solution(arr1, arr2):
    answer = []
    Number = len(arr1)
    for i in range(Number) :
        tempNumber = len(arr1[i])
        templist = []
        for j in range(tempNumber) :
            summ = arr1[i][j] + arr2[i][j]
            templist.append(summ)
        answer.append(templist)
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))

# 다른 사람의 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer