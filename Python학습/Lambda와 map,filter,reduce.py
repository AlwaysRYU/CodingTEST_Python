# Lambda
'''
형식 :
    lambda 인자 : 표현식 
'''

# 람다형식으로 표현하기
# 형식1 : 밑에서 변수가 2개라서 괄호에다가 2개만 넣어야함.
print((lambda x,y : x + y)(10,20))
# 형식2 : range()를 사용
print(list(map(lambda x : x **2 , range(6) )))

# 형식4 : lambda로 정렬 할때, 두가지 조건을 줄때
listt = ['ab','bc','cd','aaa','bca']
sorted(listt, key = lambda x : (len(x), x))
# 위의 코드는, listt를 길이순으로 정렬하고, 같은 길이에서는 알파벳으로 정렬한다.

# 형식5 : 함수 바꾸는 예제
def add(x) : return x + 10 
add2 = lambda x : x + 10

# 형식6 : lambda if 함수 사용방법 
def score(x) :
    if x > 80:
        return 'pass'
    else :
        return 'fail'
score2 = lambda x : 'pass' if x>= 10 else 'f'
# if 문이 true 일때 앞부분, else 일때는 뒷부분

#map
'''
의미:
    map은 리스트의 요소를 지정된 함수로 처리해주는 함수이다.
    함수와 리스트를 인자로 받고,
    리스트로부터 함수를 적용시키고, 새로운 리스트에 담아준다.
    출력이 리스트인 것이다.
    list(map(함수, 리스트))
    tuple(map(함수, 리스트))
    이런식으로 가능하다.
형식:
    map(함수, 리스트)
'''
# 반복가능한 개체란?
# https://dojang.io/mod/page/view.php?id=2405

# 예시 1
# 01234 를 제곱하여서 리스트로 저장
print(list(map(lambda x : x**2 , range(5) )))

# 예시 2 : 인트문
a = [1.2, 2.5, 3.7, 4.6]
print(list(map(int,a)))

# 예시 3 : input() 까지
a = map(int, input().split())
