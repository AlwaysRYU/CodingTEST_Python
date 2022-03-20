# 소수찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839



import itertools

def solution(numbers):
    answer = 0
    array = []
    for i in numbers :
        array.append(int(i))
    print(array)
    Number = len(array)

    nCr = []
    for i in range(1,Number+1):
        temp = list(itertools.combinations(array,i))
        print(temp)
    print(nCr)
    return answer


numbers11 = "17"
numbers22 = "011"

print(solution(numbers11))
print(solution(numbers22))


# 나의 풀이 조합 -> 같은 것을 제거 
# def solution(Arr) :
#     nCr = list(itertools.combinations(Arr,2))
#     print(nCr)
#     i = 0
#     while i < len(nCr) :
#         a, b = nCr[i]
#         if a == b :
#             del nCr[i]
#             continue
#         else:
#             i += 1
#     return len(nCr)

# print(solution([1,3,2,3,2]))
# print(solution([1,5,4,3,2,4,5,2]))