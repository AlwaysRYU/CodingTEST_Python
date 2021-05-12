# 파이썬에서의 집합
# set()을 이용한다.

p1 = set([1,2,3,4,5])
p2 = set([6,7,8,9,10])

# 1. 합집합
# | 또는 union 사용
print(p1 | p2)
print(p1.union(p2))

# 2. 차집합
# - 또는 difference 사용
print(p1-p2)
print(p1.difference(p2))


# 3. 교집합
# & 또는 intersection 사용
p1 = set([1,2,3])
p2 = set([1,5,6])
print(p1&p2)
print(p1.intersection(p2))


# 4. 집합에 값 추가
# add
p1.add(5)

# 4-2. 집합에 여러값 추가
# update 
# 단,리스트로 해야함
p1.update([6,7,8])

# 5. 집합 값 삭제
# remove
p1.remove(5)


# 6.frozenset
# 데이터를 수정할수 없는 집합
p3 = frozenset([1,3,5])
print(p3)


# 특 : 중복
p4 = set([1,2,3,3,3,9,9])
p4.add(2)
print(p4)


