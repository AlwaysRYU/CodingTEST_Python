# 리스트 관련 메소드, 팁 정리
# https://wikidocs.net/14
# https://wikidocs.net/16040

# 1. list에 원소 추가 
a = [0,1,2,3,4,5,6,7,8,9]

# 1-1. append(값) : 값을 맨뒤에 입력
a.append(10)
# 1-2. insert(인덱스, 값) : 특정 인덱스에 값을 입력
a.insert(12,11)
print(a)
# 1-3. extend([리스트]) : 리스트를 뒤에 붙인다.
a.extend([12,13,14])
print(a)
# 1-4. + 를 사용해서 더할 수 도있다.
a += [15,16,17]
print(a)

# 2. 원소 삭제
b = [1,1,4,2,3,4,5]
print()
print(b)

# 2-1. del(주소) : a[i] 의 위치의 요소를 삭제한다.
del b[2]
print("리스트 : " + str(b))
# 2-2. remove(값) : 특정한 값을 삭제한다. 같은 값일 경우 앞의 요소를 삭제한다.
b = [1,1,4,2,3,4,5]
b.remove(4)
print(b)
# 2-3. 리스트안의 특정한 요소를 모두 삭제하고 싶을 때는.
x = [1,2,3,2,2,2,3,4]
filter(lambda a: a!=2, x)
# 2-4. pop() : 리스트의 맨 마지막요소를 돌려주고 , 삭제한다.
x.pop()
x.pop(3) #이렇게 사용도 가능하다. pop(z) z-1번째 요소(a[z])를 뺀다는 뜻이다.

# 3. reverse() : 뒤집기
x.reverse()

# 4. count() : 리스트 포함된 요소의 개수 세기
x.count(4)

# 5. index(값) : 위치반환
a = [7,8,9]
a.index(7)

# 6. sort,sorted : 정렬, 반환하진않는다.
a.sort(reverse=True) #내림차순
sorted(a) # 이런식으로 사용가능
'''
key를 사용할 수 있다. 이건 많이 쓰더라.
key:
    정렬을 목적으로 하는 함수를 값으로 넣는다.
    lambda를 넣어서 사용하기도 함.
'''
b = ['judgment', 'compare','you','gryffin','car','thegarden']
print(sorted(['1','12','123','1234','12345'], key = len))
# 또는
print(sorted(b, key = lambda x : x[1]))
# 두번째 글자로 배열

# 여러 개로도 가능하다.
sorted(["abcd","sun","aun","gdull","eugd","quee","auee","quaa"], key = lambda x : (x[0],x[1]))



# 반복문으로 이중리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
# 00  2열 3행
# 00
# 00


# 뒤에서부터 역순 출력 : 리스트 슬라이스
a = [1,2,3,4,5,6,7,8,9]
for i in a[::-1]:
    print(i)

# 팁 리스트와 문자열 변환하기
# split() : STR형을 리스트로 바꿀때
munjang = "Asgore attacked me with spear"
a = munjang.split()
print(a)
# 또는 한글자씩 바꿀 때
name = "Author"
a = list(name)
print(a)


# ''.join(리스트) : 반대로, 리스트를 STR로 바꿀때
new_name = ''.join(a)
print(new_name)

# 파이썬에서 리스트 안의 값을 바꿀 때
print()
print("swap")
list_a = [3,5]
list_a[0], list_a[1] = list_a[1], list_a[0]
print(list_a)
# 이렇게 바꿀수 있다.