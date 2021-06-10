# 2개 이하로 다른 비트
# https://programmers.co.kr/learn/courses/30/lessons/77885

# Ver. 1
def F1(x):
    n = x + 1
    while True :
        dif = bin(x ^ n).count("1")
        if dif <= 2 :
            break
        n = n + 1
    return n
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

def F3(x):
    bina = "0" + bin(x)[2:]
    ans = ""
    for i in range(len(bina)-1, -1, -1):
        if bina[i] == "0" :
            # del answer[0]
            # answer.insert(0,0)
            # answer.insert(0,1)
            ans = "10" + ans[1:]
            break
        else:
            # answer.insert(0,1)
            ans = "1" + ans
    return int("0b" + ans , 2)


print(F3(7))

def solution2(numbers):
    answer = []
    for i in numbers :
        if (i%2) == 0:
            answer.append(i+1)
        else:
                answer.append(F3(i))
    return answer 

print(solution2([2,7]))