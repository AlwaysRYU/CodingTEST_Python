# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309


# 나의 로직
# 9명이니까, 2명씩 빼보고 구하자.

# 9 명 입력받기
shortie = []
for i in range(9) :
    shortie.append(int(input()))
print(shortie)

answer = []

for i in range(9):
    temp = shortie.copy()
    del temp[i]
    for j in range(8):
        temp2 = temp.copy()
        del temp2[j]
        if (sum(temp2) == 100 ) :
            answer = temp2.copy()

answer.sort()

for i in range(len(answer)) :
    print(answer[i])


# 다른 사람의 풀이
# 원본 해치지 않으려고 copy()쓰면서 했는데, 굳이 그럴필요가 없는 문제이다.
# 정렬된 리스트로 만들기 
l = sorted(int(input())for i in range(9)) 

for i in l:
    for j in l:
        # 이게 포인트 인듯
        if i+j == sum(l)-100 :
            # 100 == sum(l) -i-j 가 더 직관적이다.
            l.remove(i)
            l.remove(j)
            break
for i in l:
    print(i)