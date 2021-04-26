# 파이썬 내장함수 정리
# https://wikidocs.net/32

# abs

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

# eval
# filter
# hex
# id
# input
# int
# isinstance
# len
# list
# map
# max
# min
# oct
# open
# ord
# pow
# range
# round
# sorted
# str
# sum
# tuple
# type
# zip