# H-index
# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

c = [3,0,6,1,5]
c1, c2, c3, c4 = [31,66], [0,1,1], [0,1], [0, 1, 3, 5, 5, 5, 5, 5, 5, 6] 

# 나의 풀이
def solution(cc):
    answer = 1
    cc.sort(reverse=True)
    print(cc)
    if cc[0] == 0 : return 0
    if cc[1] == 1 : return 1
    for i in range(1, len(cc)):
        if cc[i] > answer:
            answer += 1
    return answer 

# 다른 사람의 풀이
def solution2(citations):
    answer = 0
    citations.sort()
    num = []
    for i in range(max(citations)+1):
        ct = 0
        for val in citations:
            if val >= i:
                ct = ct+1
            else:
                ct = ct+0
        num.append(ct)

        if num[i] >= i:
            answer = i
        else:
            break

    return answer

print(solution(c))
print(solution2(c))
print(solution(c1))
print(solution2(c1))
print(solution(c2))
print(solution2(c2))
print(c3) # 테스트케이스 11번
print(solution(c3))
print(solution2(c3))
print(c4)
print(solution(c4))
print(solution2(c4))