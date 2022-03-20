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


#min() 리스트에서 최소값 찾기
#max() 리스트에서 최대값 찾기
print(max(a))

#len() 리스트의 길이를 구하기.
#출력 : 1부터,,
print(len(a))

#del() 리스트 요소 삭제하기
#del a[x] x번째 요소값을 삭제 

# append() 리스트에 요소 추가
# a.append(4) a리스트에 4를 맨뒤에 추가.

# index() 위치반환
# a.index(3) 3이라는 요소가 있는 위치를 출력

# insert() 요소 삽입
# a.insert(0, 4)  a리스트에 0번째에 4를 삽입.

# pop()  맨마지막 요소를 돌려주고 반환.

# set 리스트의 중복을 제거
set(a)