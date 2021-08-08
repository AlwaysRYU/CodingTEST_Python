# 연산자 끼워 넣기 
# https://www.acmicpc.net/problem/14888



# N = int(input())
# number = input().split(" ")
# # kiho = [0 for _ in range(4)]
# kiho = input().split(" ")
# array = []
# for i in range(4) :
#     if i == 0 :
#         temp = '+'
#     elif i == 1 :
#         temp = '-'
#     elif i == 2 :
#         temp = '*'
#     elif i == 3 :
#         temp = '/'
#     for j in range(int(kiho[i])):
#         array.append(temp)
# print(array)
# answerlist = [] 

# stack = []

# first = int(number[0])

# # C개의 문자중 L개를 추출하는 함수이다.
# def crypto2(index, dep, L, C, Sum) : # dep 깊이 index 주소, L C 는 조건과 같다.
#     if (dep == L ) : # 들어간 깊이가 L, 즉 4일경우 암호 후보안에다가 넣어준다.
#         # password = ''.join(map(str, stack)) # stack에는 한글자씩 저장되어있으므로 바꿔준다.
#         answerlist.append(Sum)
#         return # 그리고 함수 종료

#     for i in range(index,C) : # index 부터 C 까지 / 처음에는 0~6 까지 / 1~6가지
#         if array[i] == '+' :
#             stack.append(array[i]) # 해당 인덱스에 글자를 넣고,
#             crypto2(i+1,dep+1,L,C, Sum + int(number[i+1]))

#         elif array[i] == '-' :
#             stack.append(array[i])
#             crypto2(i+1,dep+1,L,C, Sum - int(number[i+1]))
#         elif array[i] == '*' :
#             stack.append(array[i])
#             crypto2(i+1,dep+1,L,C, Sum * int(number[i+1]))

#         elif array[i] == '/' :
#             stack.append(array[i])
#             crypto2(i+1,dep+1,L,C, Sum // int(number[i+1]))

#         stack.pop() #그리고 빼준다. 


# crypto2(0,0,N-1,N-1, first)

# print(answerlist)


## -----------------

n = int(input())
# 연산을 수행하는 수 리스트
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i,now):
    global min_value, max_value, add, sub, mul, div

    if i == n:
        min_value = min(min_value, now)
        max_value = min(max_value, now)
    else :
        if add > 0 :
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0 :
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1
        if mul > 0 :
            mul -= 1
            dfs(i+1, now * data[i])
        if div > 0 :
            div -= 1
            dfs(i+1, int(now/data[i]))
            div += 1
dfs(1,data[0])

print(max_value)
print(min_value)