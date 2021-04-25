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
    일반적으로 O(n^2)
'''

# 퀵 정렬
'''
의미:
    기준을 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 교환 후, 리스트를 반으로 나눈다.
    기준 데이터를 설정하고, 그 기준보다 작은 데이터의 위치를 바꾼다.
    기준 = pivot
'''

def quicksort(array, start, end):

    
    return array

print("퀵정렬 : ")
print(quicksort(a,2,7))