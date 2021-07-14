# 홀수만 더하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1


# 리스트로 입력 받기
N = int(input())
array = []
answer = []

for i in range(N):
    array = [int(x) for x in input("공백을 구분자로 숫자를 입력바랍니다.").split(" ")]
    temp = 0
    for j in range(len(array)):
        if (j%2) == 1 :
            temp += j
    answer.append(temp)

for i in answer :
    print(i)
