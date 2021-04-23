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