# 농구 경기
# https://www.acmicpc.net/problem/1159

# 나의 풀이
answer = ""
dictt = {}
Number = int(input())
for i in range(Number):
    name = str(input())[0]
    
    # 딕셔너리 안에 있으면
    if name in dictt:
        dictt[name] += 1
    # 없으면 
    else :
        dictt[name] = 1
    # 딕셔너리 이용
for i in dictt :
    if dictt[i] >= 5 :
        answer += str(i)
if answer == "" :
    print("PREDAJA")
else :
    print(str(''.join(sorted(answer))))
    
# 다른사람의 풀이
import sys
input = sys.stdin.readline

D = {}
for _ in range(int(input())):
    s = input()
    if s[0] in D:
        D[s[0]] += 1
    else:
        D[s[0]] = 1
p = []
for k,v in D.items():
    if v >= 5:
        p.append(k)
if p:
    print(*sorted(p),sep='')
else:
    print('PREDAJA')