# 1. sub
# 문자열 바꾸기
'''
특정한 문자열을 찾은뒤, 다른 문자열로 바꾸는 방법
사용방법:
    re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
특징:
    count 를 사용하면 한번만 쓴다.
# '''
# abc = 'appleorangefruit'
# abc = re.sub('apple | orange', 'fruit', 'apple box orange tree')

import re

p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))
# 의미 :
#       blue와 white 를 colour로 바꾼다.