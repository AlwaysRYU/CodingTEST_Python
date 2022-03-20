# Q8 문자열 재정렬
# P.322


IN = "K1KA5CB7"
IN2 = "AJKDLSI412K4JSJ9D"

def solution(inn) :
    ENG = []
    NUM = 0

    E = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    N = "1234567890"

    for i in inn :
        if i in E :
            ENG.append(i)
        else :
            NUM += int(i)
    ENG.sort()
    ENGG = "".join(ENG) 
    return ENGG + str(NUM)
    

print(solution(IN))
print(solution(IN2))

# 다른 풀이
strr = "ABD"
for i in strr :
    if i.isalpha() : 
        break
        
        # 알파벳인지 알아보는 방법 중에 이런 방법이 있다! # 기억해두자