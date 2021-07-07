# 0. 주석
'''
방법 :
    """ """
    ctl + /
'''

# def sum(a,b) :
#     #더하기 함수
#     print(a+b)
'''
'''

# 1. split
'''
# split( seq = '', max split = -1) 문자열을 나누는 함수
# seq : 문자열을 구분하는거
# maxsplit : 분리할 문자개수를 지정할 때 사용됨
'''
# examplemal = '우리는 모두 괜찮습니다.'
# print(examplemal)
# examplemal.split(' ')
# print(examplemal)


# 2. for 문
# for 변수 in 리스트 :
exlist = ['one', 'two', 'three']
for i in exlist:
    print(i)

# 2-1. for else
# 파이썬은 for else 를 쓸 수 있다.
# for이 중간에 break로 끊기지 않고 끝까지 수행됐을 때 수행하는 코드이다. 
for i in range(11):
    if i == 4:
        print("빠져나갔다.")
        break
else :
    print("안빠져나가고 종료됨")
print()


# 3. range
# 숫자 리스트를 자동으로 만들어주는 range 함수

add = 0
for i in range(1,11):
    add = add + i
print(add)

# 4. iterator 이터레이터
# 파이썬에서 반복자는 여러개의 요소를 가지는 컨테이너(리스트, 튜플, 셋, 사전 문자열)에서 각 요소를 하나씩 꺼내 수행하는 간편한 방법을 제공하는 객체


# 5. map
'''
    map(f, iterable)은 함수 f와 반복가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 f가 수행한 결과를 묶어서 돌려주는 함수이다. 
    map(적용시킬 함수, 적용시킬 요소)
    map(함수, 리스트)
'''
#리스트 데이터를 두배를 곱하는 함수
def two_times(alist):
    result = []
    for number in alist:
        result.append(number*2)
    return result

result1 = two_times([1,2,3,4])
print(result1)

def two_times2(nn):
    return nn*2

list2 = map(two_times2, [1,2,3,4])
print(list(list2))



# 6. lambda
'''
함수의 재사용의 목적이 없다면 lambda로 바꿔도 된다.
함수를 딱 한줄만으로 만들게 해주는 친구.
lambda 인자 : 표현식
'''
#xy의 합을 구하는 함수
def hap(x,y):
    return x + y
print(hap(10,20))
#를 lambda로는 이렇게 표현 가능
(lambda x,y : x + y)(10,20)


#map과의 차이
#이건 x값을 제곱하라는 함수
list(map(lambda x: x**2, range(5)))


print('파이썬의 언더스코어')
#7. 파이썬의 언더스코어 _
'''
파이썬의 언더스코어 _
값을 무시하고 싶을 때 / 변수에 특별한 의미를 부여할대, 제화 함수로 사용할 때
1. 마지막으로 실행했던 결과 값이 _ 라는 변수에 저장
2. 값을 무시하고 싶은 경우
'''
x, _, y = (1, 2, 3,)
print(x, y)
x, *_, y = (1,2,3,4,5,6,7,8)
print(x,y)

for _ in range(3):
    print("악")
# 따로 i를 사용하지 않아도 반복문 이가능하다.


# 8. 리스트의 슬라이스
# https://dojang.io/mod/page/view.php?id=2208
'''
a[0:4] 는 인덱스 0 부터 3까지 잘라서 새리스트를 만드는 것.
중요한 것은 -1 과 같이 음수를 인덱스로 지정할 수 있단 것.
a[4:-1]
-1 은 뒤에서 첫 번째 요소를 말한다.즉, 맨마지막요소이다.
-2 는 뒤에서 두 번째 요소를 말한다.
a[2:8:3]
이건, 인덱스 2부터 3씩 증가시키면서 7까지 가져오겠다는 말이다.
생략도 가능하다.
a[:7]
리스트의 처음부터 인덱스 6까지 가져오겠다는 말이다.
마지막은 역시
a[7:]

인덱스 증가폭을 음수로 지정할 경우,
a[5:1:-1]
인덱스 5부터 2까지 1씩 감소하면서 가져오겠다

range에서도 사용이 가능하다.
range(0, 7, 2)
0 부터 2씩 증가시키면서 인덱스 6까지 숫자 4개를 생성하는 range객체를 만든다

'''
print('리스트의 슬라이스')
a = [0,1,2,3,4,5]
print(a[-1:])

# 2021.04.14.
# 9. sorted() 내장함수
# https://docs.python.org/ko/3/howto/sorting.html
'''
파이썬 리스트에는, 새로정렬된 리스트를 만드는 sorted()내장함수가 있다.
예를들어,
sorted([5,2,3,1,4])  라고하면
[1,2,3,4,5]가 출력된다.
역시 reverse = True 로 역정렬이 가능하다.
'''


# 2021.04.14.
# 10 zip() 내장함수
# https://www.daleseo.com/python-zip/
'''
두 그룹의 데이터를 엮어주는 파이썬의 내장함수 zip()
순회가능한 객체를 인자로 받고,
각 객체가 담고있는 원소를 차례로 반복하여 접근하는
반복자를 반환한다.
'''
print()
print("zip내장함수")
numbers = [1,2,3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)
for number, upper, lower in zip("12345", "ABCDE", "가나다라마"):
    print(number, upper, lower)


# 2021.04.21.
# 11. 이진수
'''
근데 앞에 0x 이런게 있으니까 [2:] 사용하고
bin(6|9)[2:] 이렇게 논리 연산도 가능하다.
'''


# isdigit /isalpha
# 문자열이 숫자인지 문자인지 체크하기 
'''
isdigit : 이게 숫자인지? True / False
idalpha : 이게 문자인지? True / False
'''

num = '111'
print()
print(num.isdigit())
print()


# 12.연산자
'''
산술에서 신경쓸 것은  //은 몫, /은 나누기
'''

# 13. 문자열.replace(a,b) : 특정한 값 교체
'''
replace(a,b,c) : a를 b로 교체한다. c는횟수.
문자열에서만 사용가능 
하나만 할 수있다.
""를 통해 문자열에서 특정 문자을 제거 할 수 있다.
'''


# 14. 무한대 표시
'''
알고리즘 풀이시 최소값, 최대값 구할 때 사용하는 무한대.
두가지 방법이 있다.
math 를 임포트해서도 가능하다.
'''
# 무한대 float 만 가능하다.
positive = float('inf')
print(positive)
negative = float('-inf')
print(negative)

# if문 한줄로 사용하기
print("if 문 사용법 " )
if x > 0 :
    value = 10
else :
    value = 20
#을, 한줄로 표현하기
value = 10 if x > 0 else 20
# 또,
alpha = 0
if alpha > 7 :
    beta = 999 
elif alpha == 7 :
    beta = 99
else :
    beta = 0
#를 ,한줄로 표현하면 (elif를 표현하는 것이다.)
beta = 999 if alpha > 7 else ( beta == 99 if alpha == 7 else 0 )
# 이걸한다. 만약 A면, A가 아니면 else 구문을 한다.
beta = {alpha > 7: 999, alpha < 7: 0}.get(True, 99)
# 또는, 이렇게 표현가능하다.


# 15. 문자열 (str) 관련 함수
# find -> 리스트의 index같은거
"abcdefg".find("a") #하면 0이 출력된다.