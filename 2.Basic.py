# 0. 주석 달기
# 주석다는 방법 : ''' """
# 또는 ctl + /

# def sum(a,b) :
#     #더하기 함수
#     print(a+b)

# 1. split
# split( seq = '', max split = -1) 문자열을 나누는 함수
# seq : 문자열을 구분하는거
# maxsplit : 분리할 문자개수를 지정할 때 사용됨

# examplemal = '우리는 모두 괜찮습니다.'
# print(examplemal)
# examplemal.split(' ')
# print(examplemal)


# 2. for 문
# for 변수 in 리스트 :
# ...

list = ['one', 'two', 'three']
for i in list:
    print(i)


# 3. range
# 숫자 리스트를 자동으로 만들어주는 range 함수

add = 0
for i in range(1,11):
    add = add + i
print(add)
