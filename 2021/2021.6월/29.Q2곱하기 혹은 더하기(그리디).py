# 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며,
# * + 를 넣어 결과적으로 만들어 질 수 있는 가장 큰 수를 만드는 프로그램을 작성하시오.
# ex ) 02984 -> 576
# ex ) 567 -> 210

Numberr= map(str, input("문자열 입력 : "))

def solution(Strr) :
    answer = 1
    for i in Strr :
        Num = int(i)
        if Num == 0 :
            continue
        elif Num == 1 :
            answer += 1
        else:
            answer *= Num
    return answer
# 0 1 은더하고, 나머지는 곱하는 것이 무조건 최대가 나온다.
            
print(solution(Numberr))
