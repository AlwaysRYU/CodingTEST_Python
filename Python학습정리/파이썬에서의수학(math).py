# 실수값의 오차

print( 0.1 + 0.2 == 0.3 )
# 파이썬에서 0.1 + 0.2는 0.3000000..00004임 
# 왜? 부동소수점 방식이라서 그렇다.

# 부동소수점?
'''
컴퓨터가 ..무한 소수를 표현할때 근사치로 전환한다.
'''

import math

print(math.isclose(0.1 + 0.2, 0.3))

# 1. 올림, 내림, 반올림
print(math.ceil(3.14))
print(math.floor(3.14))
print(round(3.14))

# 분수식 표현 - 내장라이브러리 : Fractions
from fractions import Fraction
# 분수를 사용할  수 있다.
number1 = 1/3 # 1/2를 저장한다.
number2 = Fraction(1,3)
print(number1 == number2) # 같지않다.
