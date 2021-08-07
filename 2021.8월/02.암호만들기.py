# 암호만들기
# https://www.acmicpc.net/problem/1759
# DFS문제 ---- 스택 , 재귀

# 입력받기
L, C = map(int, input().split()) # 각각 수를 입력받는다.
array = input().split() # array 리스트에 문자열 형태로 각각 저장된다.
array.sort() # array를 정렬한다. / 알파뱃 순으로 해야하기 때문에

# DFS용 스택 생성한다.
stack = []
# 모든 암호의 후보들을 보관하는 리스트를 생성한다. (모음 자음 계산은 아직 하지 않았다.)
answerlist = []
# 임시 리스트이다. answerlist에 저장할 리스트다.
temp =[]

# C개의 문자중 L개를 추출하는 함수이다.
def crypto2(index, dep, L, C) : # dep 깊이 index 주소, L C 는 조건과 같다.
    if (dep == L ) : # 들어간 깊이가 L, 즉 4일경우 암호 후보안에다가 넣어준다.
        password = ''.join(map(str, stack)) # stack에는 한글자씩 저장되어있으므로 바꿔준다.
        answerlist.append(password)
        return # 그리고 함수 종료

    for i in range(index,C) : # index 부터 C 까지 / 처음에는 0~6 까지 / 1~6가지
        stack.append(array[i]) # 해당 인덱스에 글자를 넣고,
        crypto2(i + 1, dep+1, L, C) # 다음 인덱스와 깊이로 넘겨서 다시 재귀호출한다.
        stack.pop() #그리고 빼준다. 

crypto2(0,0,L,C)

def showpw(list) :
    for i in list :
        ja = 0
        mo = 0
        for j in i :
            if j in 'aeiou' :
                mo += 1
            else :
                ja += 1
        if (mo >= 1 and ja >= 2) :
            print(i)
showpw(answerlist)


# def crypto(index, dep) :
#     print(index, dep)
#     # 만약 dep == 4 면 출력한다.
#     if (index == 5) :
#         return
#     if (dep == 4):
#         for i in range(C):
#             # if( istrue[i] == True ) :
#             #     print(array[i] + " ", end= "")
#             print(temp)
#         return

#     # 지금 글자를 넣고, 다음 거를 호출하기 
#     istrue[index] = True 
#     temp.append(array[index])
#     crypto(index+1, dep+1)
#     # 지금 글자를 넣지 않고, 다음 거를 호출하기
#     istrue[index] = False 
#     del temp[index]
#     crypto(index+1, dep)

