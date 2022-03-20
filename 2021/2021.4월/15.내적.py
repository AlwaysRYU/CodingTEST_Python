# 내적
# 2021.04.14
# https://programmers.co.kr/learn/courses/30/lessons/70128
'''
길이가 같은 두 1차원정수 배열 a,b가 매개변수로 주어진다.
a,b의  내적을 return 하도록 
solution 함수를 작성하라.
내적이란
a[0]*a[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]
이다. (n은 a,b,의 길이)
'''

aa = [[1,2,3,4], [-3,-1,0,2]]
bb = [[-1,0,1], [1,0,-1]]

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += (a[i] * b[i])
    return answer

# 다른 사람의 풀이
def solution2(a, b):
    return sum([x*y for x, y in zip(a,b)])

print(solution(aa[0],aa[1]))
print(solution(bb[0],bb[1]))