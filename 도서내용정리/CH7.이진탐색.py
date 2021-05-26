# Ch. 7 이진탐색

# 순차탐색코드
print("순차탐색코드")
'''
의미 :
    앞에서부터 순서대로 탐색하기.
시간복잡도 : 
    최대 O(n)
'''

# 이진탐색
'''
의미 :
    반으로 쪼개면서 탐색하기
    단, 배열 내부가 정렬되어있어야만 사용 가능하다.
시간복잡도 :
    O(logN)
'''
print("이진탐색 구현 (재귀) : ")
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def binary_s(target,arr):
    if len(arr) == 0 :
        return print("없음")
    
    mid = len(arr) // 2
    if arr[mid] == target :
        return mid
    elif arr[mid] > target :
        return binary_s(target, arr[:mid])
    elif arr[mid] < target :
        return binary_s(target, arr[mid:])

print("위치는 ")
print(binary_s(4,array) + 1)
# print(binary_s(2,[0,1,2,3,4]))

