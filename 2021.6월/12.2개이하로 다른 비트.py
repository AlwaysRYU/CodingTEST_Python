# 2개 이하로 다른 비트
# https://programmers.co.kr/learn/courses/30/lessons/77885

# 최종 제출 형 (나의풀이)
def F3(x):
    bina = "0" + bin(x)[2:]
    ans = ""
    for i in range(len(bina)-1, -1, -1):
        if bina[i] == "0" :
            ans = bina[:i] + "10" + bina[i+2:]
            break
    return int("0b" + ans , 2)

def solution2(numbers):
    answer = []
    for i in numbers :
        if (i%2) == 0:
            answer.append(i+1)
        else:
            answer.append(F3(i))
    return answer 

# 다른 사람의 풀이

# 다른사람의 풀이
def solution3(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer

# 나처럼 푼사람이 없다.
# 일일히 하기는 힘들다는것을 았고, ^을 쓰려고했는데 다른사람은 잘썼네
# 나는 이진법의 수학적 접근으로 풀었다.
# 다른사람은 코딩으로 푼듯.


# Ver. 1
def F1(x):
    n = x + 1
    while True :
        dif = bin(x ^ n).count("1")
        if dif <= 2 :
            break
        n = n + 1
    return n

# for i in range(1, 51, 2):
#     print(str(i) + " -> "+ str(F1(i)))

# 이방법은 시간초과 뜬다......
# 요즘 계속 시간초과 뜨네
# 저 dif = bin(x6n).count("1")에서 문제가 되는 거 겠지.

# Ver. 2 : count를 안씀
def F(x):
    temp = x
    tempn = x + 1
    n = x + 1
    Dalla = 0 
    while True :
        print( "지금 비교 하는 수 X : " + str(temp))
        print( "지금 비교 하는 수 temp : " + str(tempn))
        ModA = temp % 2 
        ModB = tempn % 2
        print(ModA, ModB)

        if ModA == ModB :
            if tempn == 0 and temp == 0 :
                return n
            temp = (temp // 2)
            tempn = (tempn // 2)

        else :
            Dalla += 1
            if Dalla == 3 :
                print( "-----------초기화------------")
                Dalla = 0
                n += 1
                # 초기화
                tempn = n
                temp = x
                print("n은 " + str(n))
                continue
            if tempn == 0 and temp == 0 :
                return n
            temp = (temp // 2)
            tempn = (tempn // 2)
        
    return n
# 이방법도 시간 초과 뜬다.


def solution(numbers):
    answer = []
    for i in numbers :
        answer.append(F(i))
    return answer

# 왜?
# 수를 '찾는' 것이 문제인가?
# 수를 '만들'어야 하나..?
# 짝수면 -> 맨끝만 바꾸면 땡임
# 홀수면 -> 맨끝에 서부터 
print(solution2([2,7]))

