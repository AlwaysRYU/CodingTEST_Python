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
# 마우스 팽귄은 키, 3, 5는 값
mydictionary = {"mouse" : 3, "penguin" : 5 }
dic = { 'name' : 'maya pay' , 'phone': '010545' }
a = { 1: [1,2,3], 2 : [4,5,6]}
mydictionary["cat"] = 1
print(mydictionary)


# 0. 딕셔너리 호출 : key를 이용해서 value를 호출한다.
print(mydictionary["mouse"])
#이러면 3이 출력된다.

# 1. 딕셔너리에 쌍 추가
# a[키] = 값
a[3] = [7,8,9]
print(a)

# 2. 딕셔너리 요소 삭제
# del a[키]
del dic['name']

# 3. 딕셔너리 관련 함수
# 3-1. items()
# key value 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
# 리스트로 사용할 수 있다.
print(a.items())
templist = a.items()
print(templist)

# 3-2. keys()
# 딕셔너리의 키만 모아서 객체를 돌려준다.
print(list(a.keys()))

# 3-3. values()
# 마찬가지로 value만 모아서 돌려준다.

# 3-4. clear()
# 딕셔너리 안의 모든 요소를 삭제한다.

# 3-5. get()
# key 로 value 얻기
# dictionary.get(key)

print(mydictionary.get('mouse'))
# 또는
print(mydictionary.get('spiderman','없음'))
# key에 해당하는것이 없을 경우, 오른쪽을 돌려준다.


