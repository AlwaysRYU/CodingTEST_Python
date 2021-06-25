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
print(solution(121))


# def solution2(n):
#     answer = 0
#     answerlist = [ i for i in range(n+1) ]
#     print(answerlist)


# print(solution2(10))
# print(solution2(121))


def solution4(n) :
    num = set(range(2, n+1))
    for i in range(2,n+1): 
        if i in num :
            num -= set(range( 2*i , n+1, i))
    return len(num)
# 실시간으로 바꿔주는 방법을 사용할 줄 알아야한다.
# 다음에 다시 풀어보자.
print(solution4(121))