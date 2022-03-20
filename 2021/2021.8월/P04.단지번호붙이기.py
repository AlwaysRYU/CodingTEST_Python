# 단지번호 붙이기
# https://www.acmicpc.net/problem/2667
# 
# 

import sys
sys.setrecursionlimit(1000000)
#깊이탐색에는 이걸 쓰도록하자.

hang = int(input())#행렬 받기
madang = [0] * hang #행렬초기화
answer = [] # 답
count = 0#카운트

for i in range(0,hang):
    madang[i] = list(map(int, input()))
#행렬 입력받기

Tx = [ -1, 0, 1, 0]
Ty = [ 0, 1, 0, -1]


def Search(a,b,Real):
    madang[a][b] = 0 #바꿔주고
    for i in range(4):
        ex = a + Tx[i]
        ey = b + Ty[i]
        if( ex >= 0 and ex < hang and ey >= 0 and ey < hang and madang[ex][ey] == 1):

            Real = Search(ex,ey,Real+1)
    return Real



for i in range(hang):
    for j in range(hang):
        if(int(madang[i][j]) == 1 ):
            answer.append(Search(i,j,1))
            count += 1
            
answer.sort()
#답 표출
print(count)
for i in range(len(answer)):
    print(answer[i])