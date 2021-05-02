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

#map
'''
의미:
    함수와 리스트를 인자로 받고,
    리스트로부터 함수를 적용시키고, 새로운 리스트에 담아준다.
형식:
    map(함수, 리스트)
'''

print(list(map(lambda x : x**2 , range(5) )))