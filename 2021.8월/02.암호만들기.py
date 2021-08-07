# 암호만들기
# https://www.acmicpc.net/problem/1759


L, C = map(int, input().split())
array = input().split()

istrue = [ False for i in range(C)]
print(istrue)
print(L)
print(C)
print(array)
array.sort()
print(array)

temp =[]

def crypto(index, dep) :
    print(index, dep)
    # 만약 dep == 4 면 출력한다.
    if (index == 5) :
        return
    if (dep == 4):
        for i in range(C):
            # if( istrue[i] == True ) :
            #     print(array[i] + " ", end= "")
            print(temp)
        return

    # 지금 글자를 넣고, 다음 거를 호출하기 
    istrue[index] = True 
    temp.append(array[index])
    crypto(index+1, dep+1)
    # 지금 글자를 넣지 않고, 다음 거를 호출하기
    istrue[index] = False 
    del temp[index]
    crypto(index+1, dep)


crypto(0,0)


