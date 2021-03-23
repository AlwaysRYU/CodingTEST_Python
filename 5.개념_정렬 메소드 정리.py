#list.sort
'''
리스트 정렬 메소드들
'''
a = [1, 10, 5, 7, 6]

# reverse -> 리스트를 거꾸로 뒤집는다.
a.reverse()
print(a)

# sort -> 오름차순 정렬
# sort(reverse=True) -> 내림차순 정렬
a.sort(reverse=True)
print(a)

# 분리
m = '우리는 모두 괜찮은 존재입니다.'
m = m.split()
print(m)

m.sort(key=len)
print(m)
#len은 길이 -> 따라서 길이순으로 정렬된다.