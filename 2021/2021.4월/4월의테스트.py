#lambda
'''
람다란?
lisp 에서 받음
함수를 한줄로 만들어주는 함수

lambda 인자 : 표현식

'''
#x+y를 합하는 함수
def hap(x,y) :
    return x + y

print(hap(10,20))

#이걸 lambda로
print((lambda x, y: x+y) (10, 20))

# map 함수
'''
map은 함수와 리스트를 인자로 받는다.
리스트로부터 원소를 하나씩 꺼내서 함수를 적용시키고, 새로 리스트를 담는다.
map(함수, 리스트)
'''

print(list(map(lambda x: x**2, range(5))))
#파이썬 3에서는 list를 앞에 써줘야한다.
'''
위의 map 함수가 받은 함수
lambda x : x **2 
리스트 는
range(5) -> 즉 [0,1,2,3,4]라는 뜻
'''


#reduce 함수
'''
reduce(함수, 순서형 자료)
원소를 누적적으로 함수에 적용시키는 것.

'''


