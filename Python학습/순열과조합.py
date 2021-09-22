# 순열
# 몇개를 골라 순서를 고려해 나열한 경우의 수
'''
N 개중 R개를 골라서 순서를 정해 나열하는 가짓수
nPr

permuations
'''

import itertools

# 3P2
arr = ['A', 'B', 'C']
nPr = list(itertools.permutations(arr,2))
print(nPr)
print(len(nPr))


#조합
#서로다른 n개중에서 r개(n>r)를 취하여 조를 만들 때 하나하나의 조
#순서를 고려하지 않음

# import itertools 해주고

nCr = list(itertools.combinations(arr,2))
print(nCr)


# 쓰는 방법

c = 5

from itertools import combinations

for i in range(1,c):
    print(list(combinations(range(c),i)))

'''
특징:
    문자열 가능. 'abcd' -> 'a', 'b', 'c','d' 같이 가능하다.
'''