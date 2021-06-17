# 효율적인 화폐구성
# P.226


'''
2 3 - > 15  출력 5 개
3 5 7 -> 4  출력 -1 (불가능)
'''

W1, W1 = [2,3], 15
W2, W2 = [3,5,7], 4

def solution(Array, Won) :
    answer = 0
    
    Array.sort()
    if Array[0] > Won :
        return -1




    return answer 


n,m = map(int, input().split())
d = [10001] * (m + 1)
array = []
d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 1001 :
            d[j] = min(d[j], d[j - array[i]] + 1)



