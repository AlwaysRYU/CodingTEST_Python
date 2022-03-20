# 약수의 합 외 3문제
# 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3

def solution(n) :
    answer = 0
    temp = n//2
    for i in range(1):
        if n % i == 0 :
            answer += i
            # answer += (n//i)
            # print(n//i, i)

    return answer

print(solution(12))


# 핸드폰 번호 가리기
def solution2(phone_number):
    leng = len(phone_number) - 4
    answer = '*' * leng  + phone_number[-4 : ]
    return answer



# 하샤드 수
def solution3(x):
    strr = str(x)
    temp = 0
    for i in strr :
        temp += int(i)
    if x % temp == 0 :
        return True
    else :
        return False

# 콜라츠 추측
def solution4(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            answer += 1
        else :
            num =( num * 3 ) + 1
            answer += 1

        if answer >= 500 :
            return -1
    return answer