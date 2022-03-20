# 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

# 나의 풀이
def solution(n):
    answer = 0
    di = (n//2) + 1
    for i in range(1,di):
        temp = 0
        J = i
        print("I : " + str(i) )
        while True :
            temp += J
            print("지금 현재 더하는 수 : " + str(temp))
            if temp == n :
                answer +=1
                print("YES")
                break
            elif temp >= n:
                break
            J += 1
        
    return answer + 1


print(solution(15))

# 다른사람의 풀이
# 다 비슷하게 풀었다.