# Counter 클래스
'''
의미:
    어떤 단어가 주어졌을 때, 단어에 포함된 각 알파벳의 글자 수를 세어주는 간단한 함수이다.
'''

#선언
from collections import Counter

# 예시 1 : hello word 문자열에서 각 글자가 몇 번 사용됐는가?
print(Counter('hello world'))

# 메소드 1 : most_common
# 데이터의 개수가 가장 많은 순으로 정렬된 배열을 리턴 한다.

print(Counter('you put me up, and you put me down').most_common())
# 숫자만큼 리턴함
print(Counter('you put me up, and you put me down').most_common(2))


# 특징 :
# 두 카운터를 더하거나, 뺄 수도 있다.
a = Counter(['shake it on','hot property'])
b = Counter(['space cowboy','little l','canned heat','shake it on'])
print(a)
print(b)
print(a+b)
# 뺄때는 이렇게 한다.
a.subtract(b)
print(a)


# 특징 :
# 교집합, 합집합 연산역시 가능하다.
a&b
a|b

