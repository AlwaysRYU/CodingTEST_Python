# https://programmers.co.kr/learn/courses/30/lessons/12953

a1 = [2,6,14,8]
a2 = [1,2,3]

a3 = [2,3,4] # >> 12
a4 = [1,2,3] #>> 6
a5 = [2,7,14] #>> 14
a6 = [3,4,9,16] #>> 144

def solution(arr):
    print("해볼 거 : " + str(arr))
    arr.sort()
    answer = 1
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[j] % arr[i]) == 0 :
                arr[j] = (arr[j] // arr[i])    

    for i in range(len(arr)):
        answer *= arr[i]
    return answer

print(solution(a1))
# print(a2)
print(solution(a2))
# print(a3)
print(solution(a3))
print(solution(a4))
print(solution(a5))
print(solution(a6))
print(solution([5,9,8]))
print(solution([5,5,5]))
print(solution([1,1,1,1,1,1]))
print(solution([99,11,9,3,33]))
print(solution([5,10,2,4]))
'''

def solution(arr):
    arr.sort()
    answer = 1
    for i in range(len(arr)):
        temp = i  + 1
        templist = arr
        # print(templist)
        for j in range(temp, len(templist)):

            if templist[j] % arr[i] == 0 :
                templist[j] = (templist[j] // arr[i])    

            if j == (len(arr)) -1 :
                    answer = answer * arr[i]
                    arr = templist
                    arr[i] = 1
                    print(str(i) + "번째 : 전부다 나뉘어짐")
        
        answer = answer * arr[i]
        
    return answer
'''