# Dictionary
'''
개념:
    {} 를 사용하는 대표적인 타입
    key에 대응하는 value를 할당하거나, value에 접근할 때 사용한다.
    { key : Value , key2 : value2 } 
    key는 변할 수 없고, value는 변할 수 있다.
    key는 중복될 수 없다.
'''

mydictionary = {}
mydictionary = {"mouse" : 3, "penguin" : 5 }
dic = { 'name' : 'maya pay' , 'phone': '010545' }
a = { 1: [1,2,3], 2 : [4,5,6]}
mydictionary["cat"] = 1
print(mydictionary)


# 0. 딕셔너리 호출 : key를 이용해서 value를 호출한다.
print(mydictionary["mouse"])
#이러면 3이 출력된다.

# 1. 딕셔너리에 쌍 추가
a[3] = [7,8,9]
print(a)