# 위에서 아래로
# <이것이 코딩테스트다> P.178 ~ P.182
'''
문제 :
    하나의 수열에는 다양한 수가 존재한다. 이러한 크기는 크기에 상관없이 나열되어 있다.
    이수를 큰수부터 작은 수의 순서로 정렬해야한다. 수열을 내림차순으로 정렬하는 프로그램을 만드시오.
입력 : 개수 N 입력 -> N개의 개수 입력
    3 15 27 12
출력 :
    27 15 12
'''
# N을 입력 받기
'''
N = int(input("몇개의 수를 입력할 것 인가요 ? "))
array = []
for i in range(N):
    array.append(int(input("입력 : ")))
array = sorted(array, reverse = True)
print(array)
'''


# 예제 2 : 성적이 낮은 순서로 출력하기
# p.180
N = int(input("성적이 낮은 순서로 출력하기 : "))
array = []
for i in range(N):
    array.append(list(input("입력").split()))
print(array)

array2 = sorted(array, key=lambda array : array[1], reverse=True)
print(array2)

# 예제 3 : 두배열의 원소 교체 
n , k = map(int, input().split())
a = [1,2,3,4,5,6]
b = [7,8,9,10,11,12]
a.sort()
b.sort(reverse=True)

for i in range(n):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(a)
