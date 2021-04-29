# Chapter 6 정렬 (P.156 ~ )
'''
정렬?
    데이터를 특정한 기준에 따라서 순서대로 나열하는 것.
    이진탐색이 가능

'''

# 선택정렬
'''
의미:
    가장 작은것을 '선택'
과정:
    데이터 중에서 가장 작은 데이터를 선택하여 맨 앞에 있는 데이터와 바꾼다.
    그다음 작은 데이터를 선택해 두번째 데이터와 바꾼다.
    이과정을 반복한다.
'''

# 선택정렬 구현하기

a = [7,5,9,0,3,1,6,2,4,8,10,11,12]

for i in range(len(a)):
    min_index = i
    for j in range(i+1, len(a)):
        if a[min_index] > a[j]:
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]
print(a)


# 삽입 정렬
'''
의미:
    바로 정렬해서 넣기
시간복잡도:
    최선의 경우 O(n)
    일반적으로 O(n^2) 선택도 마찬가지
'''

# 퀵 정렬
'''
의미:
    기준을 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 교환 후, 리스트를 반으로 나눈다.
    기준 데이터를 설정하고, 그 기준보다 작은 데이터의 위치를 바꾼다.
    기준 = pivot
시간복잡도:
    평균 - O( N log N ) 앞선 두 정렬보다 빠르다.
    최악의 경우 - O( N^2 ) 이미 데이터가 정렬되어있는경우 등
    
'''

# 가장 널리 사용되고 있는 가장 직관적 형태의 퀵 정렬 소스 코드
b = [5,7,9,0,3,1,6,2,4,8]

def quicksort(array, start, end):
    # 원소가 1개인 경우 종료한다.
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quicksort(array, start, right -1 )
    quicksort(array, right + 1, end)    
    return array

print("퀵정렬 : ")
print(quicksort(a,2,7))

# 파이썬의 특징을 구현한 소스코드

b = [5,7,9,0,3,1,6,2,4,8]

def quickP(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면, 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot ] # pivot보다 작은 분할된 왼쪽
    right_side = [x for x in tail if x > pivot ] # pivot보다 큰 분할된 우측

    # 분할 이후 왼쪽과 오른쪽 부분에서 각자 정렬을 수행하고, 전체리스트를 반환한다.
    return quickP(left_side) + [pivot] + quickP(right_side)

print(quickP(b))


# 계수 정렬
print("계수 정렬")
'''
의미 :
    특정한 조건이 부합할 때만 사용할 수 있지만, 매우 빠른 정렬 알고리즘
    예시:
        모든 데이터가 양의 정수인 상황에서, 개수가 N, 쵀댓값이 K이 일때. 계수정렬은
        O( N + K )를 보장한다.
    계수 정렬은 이처럼 매우 빠르게 동작할 뿐만아니라 원리도 간단하다.
조건 :
    데이터의 크기 범위가 제한 되어있는 정수 형태
    예시:
        0 ~ 100 이하
특징 :
    별도의 리스트를 선언하고 정렬에 대한 정보를 담는다.
방법 :
    1. 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트를 생성한다.
    2. 리스트 안의 모든 데이터가 0이 되도록 초기화 한다.
    3. 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가 시킨다.
    4. 인덱스의 값은, 숫자가 나온 횟수이다. 인덱스에다가 값만큼 반복하여 출력하면 정렬이 완료된다.
시간복잡도 :
    O( N + K )
    기수정렬 과 더불어 가장 빠르다.
공간복잡도 :
    O(N+K)
    만약 데이터가 0 99999 두개 뿐이라면 엄청 비효율적이다.
    동일한 값을 가지는 데이터가 많을 때 적합하다.
    일반적으론 퀵을 사용합시다.
'''

e = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언
count = [0] * (max(e) + 1)

for i in range(len(e)):
    count[e[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ") #띄어 쓰기를 구분으로등장한 횟수만큼 인덱스 출력 


# 파이썬의 정렬 라이브러리
'''
현대에 정렬 알고리즘은 매우 잘 정립되어있다.
정렬 알고리즘 문제는 외우면 잘 풀 수 있을 것이다.
'''

# sorted() 함수
'''
시간복잡도 :
    O(NlogN)을 보장한다. 퀵보다는 느리다.
    병합정렬이 기반이다.
특징 :
    리스트 딕셔너리 자료형에 사용가능하다.
    결과는 리스트이다.
'''
f = [7,5,9,0,3,1,6,2,4,8]
print()
print("sorted() 함수 : ")
result = sorted(f)
print(result)

# sort()
# 별도의 리스트가 반환되지 않고, 내부 원소가 바로 정렬된다.
f.sort()

# sort(), Sorted()는 key매개변수를 입력받을 수 있다. 
g = [ ('바나나', 2), ('사과', 5), ('당근', 3), ('노래기', 7)]

def setting(data):
    return data[1]
result = sorted(g, key= setting)
print(result)

# 코딩테스트에서 나오는 정렬 알고리즘 
'''
1. 정렬 라이브러리로 풀 수 있는 문제:
    정렬 기법을 알고 있는가?
2. 정렬 알고리즘 원리에 대해 물어보는 문제
    선택, 삽입, 퀵 정렬등의 원리를 알고있는가?
3. 더 빠른 정렬이 필요한 문제 
    퀵으론 풀수없다.
    계수정렬등의 다른 정렬알고리즘을 이용하거나, 기존에 알려진 알고리즘의 구조적 개선을 거쳐야한다.
'''