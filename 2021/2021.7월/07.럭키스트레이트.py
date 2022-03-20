# 럭키스트레이트
# P.321

# 나의 풀이
def solution(number) :
    strr = str(number)
    temp = 0
    temp2 = 0
    before = strr[:len(strr)//2]
    after = strr[len(strr)//2:]
    for i in range(len(strr)//2):
        temp += int(before[i])
        temp2 += int(after[i])

    if temp == temp2 :
        return "LUCKY"
    else :
        return "READY"

print(solution(123402))
print(solution(7755))