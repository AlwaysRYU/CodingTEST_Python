# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

# 1부터  n까지 소수를 찾아서 그 개수를 반환하라.


# n은 2이 상임
def solution(n) :
    sosu = [2]
    if n == 2 :
        return 1
    issosu = True
    answer = 1
    for i in range(3,n+1):
        #소수인지 확인하고, 소수면 answer +1 한다.
        print("지금까지 소수 목록 " + str(sosu))
        for j in sosu :
            if ( i % j ) == 0 :
                issosu = False
                print(" " + str(i) + "는 소수가 아님")        
                break
        if issosu == True :
            sosu.append(i)
            answer += 1
        else :
            issosu = True
    return answer
# 시간 초과 뜸.

# print(solution(10))
# print(solution(5))

def solution2(n):
    answerlist = [] 
    for i in range(2, n+ 1) :
        if ( i //2 ) > 1 and (i % 2) == 0 :
            continue
        elif ( i // 3 ) > 1 and ( i % 3) == 0 :
            continue
        elif ( i // 5 ) > 1 and ( i % 5 ) == 0 :
            continue
        elif ( i // 7 ) > 1 and ( i % 7 ) == 0 :
            continue
        answerlist.append(i)
    print(answerlist)
    return len(answerlist)

print(solution2(5))