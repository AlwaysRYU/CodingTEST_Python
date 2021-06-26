# 소수찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921
# n까지의 소수를 찾기
def solution(n):
    answer = 0
    for i in range(2,n+1):
        if i == 2 or i == 3 or i == 5 or i == 7 :
            answer += 1
            print("수소가 아니라 소수 : " + str(i))
            continue 
        if (i % 2) != 0 and (i%3) != 0 and (i%5) != 0 and (i%7) != 0 :
            print("수소가 아니라 소수 : " + str(i))
            answer += 1
            continue
# 이건 121 부터는 판별이 불가하다.
    return answer

# print(solution(10))
# print(solution(121))
# def solution4(n) :
#     num = set(range(2, n+1))
#     for i in range(2,n+1): 
#         if i in num :
#             num -= set(range( 2*i , n+1, i))
#     return len(num)

# 집합을 사용한다.
def solution5(n):
    array = set(list(range(2,n+1)))
    print(array)
    for i in range(2,n+1):
        if i in array :
            array = array - set(range( 2*i , n+1, i ))
    return array


print(solution5(121))