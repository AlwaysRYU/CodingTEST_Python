# 파이썬 내장함수 정리
# https://wikidocs.net/32

# abs :
'''
의미 : 절대값 출력하기.
    입력
    출력:
특징 :
'''

# all :
'''
의미:
    입력 : 반복 가능한 자료형 x
    출력 :
        참이면 True
        거짓이 하나라도 있으면 False
'''
print(all([1,2,3]))
print(all([1,2,3,0]))
print(all([]))

# any
'''
의미:
    입력 : 반복가능한 자료형 x 
    출력 : 하나라도 참이 있으면 True를 반환.
'''
print(any([""]))

# bin() : 이진수 변환 
'''
의미 : 
    전달받은 integer / longinteger 자료형의 값을 2진수 (binary)로 돌려준다.
팁1 : 자동으로 자리를 맞춰서 OR연산을 해준다.
    print('OR연산')
    print(bin(arr1[i] | arr2[i]))
'''
print()
print("bin() : ")
print(bin(50))
print()
# oct() : 8진수
# hex() : 16진수
# 다른 방법 : format() 내장함수
#             여기서, #을 제거하면 맨 앞 접두어가 빠진 상태로 출력된다.
value = 50
b = format(value, '#b') #2진수
o = format(value, '#o') #8진수
h = format(value, '#x') #16진수
print(b)
print(o)
print(h)
# 다른 방법 2 : int('문자열' , 2) 
print( int(format(value, '#o'), 8)) # 50을 출력


# count : 문자열에서 해당하는 문자열이 포함되어있는지 계산해서 반환하는 함수이다.
print()
print("count() : ")
print('Zack Snyder\'s justice league'.count(' '))

print()

# chr
# dir
# divmod

# enumerate : 열거하다
'''
의미:
    입력 : 순서가 있는 자료형(리스트, 튜플, 문자열)
    출력 : 인덱스 값을 포함하는 enumerate 객체를 돌려줌.
특징:
    순서값과 함께 출력한다.
    for문과 함께 사용하면 순서와 값을 알 수 있다.
    즉, 객체가 어느 위치에 있는지 알려주는 인덱스 값이 필요할때 사용하자.
'''
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i,name)

# eval : 매개변수로 식을 받는다. 문자열(str)로!
'''
의미:
    입력 : str형 수식을 받는다.
    출력 : 계산하여 출력해준다.
특징:
    실제로는 조금 위험하다.
    이는 스크립트언어의 취약점이다.
    되도록 사용하지않는 것을 권장한다.
'''
print()
print("eval : ")
a = eval("1+3+4")
print(a)
print()

# filter

# id
# input
# int
# isinstance
# len
# list
# map
# max 와 min :
'''
의미: 각각 최대와 최소를 반환
    입력 : iterable자료형 (반복가능한 데이터 타입 / member를 하나씩 접근할 수 있는 데이터 타입)

'''

# sum : 반복가능한 객체의 요소 합
'''
의미 :
    sum(iterable, start = 0)
    iterable한 자료형을 받으며 numeric 한다.
    인자로 들어온 iterable 내부 모든 요소의 합
    start는 한 번 더 더해준다.
특징 :
'''
print("sum : ")
print(sum([2,2,2]))
print(sum([2,2,2],2))
print(sum(range(1,4))) # range도 가능하다.

# open
# ord
# pow
# range
# round

# sorted
'''
    정렬하는 함수, 리스트정리.py 참조
'''

# str

# tuple
# type
# zip

# upper / lower / isupper / islower
s1 = "SpiderMan"
print(s1.upper())