# 나누어 떨어지는 숫자 배열
# 2021.04.14. 
# https://programmers.co.kr/learn/courses/30/lessons/12910
'''
array의 각 element 중 divisor 로 나누어 떨어지는 값을
오름차순으로 정렬한 배열을 반환하는 함수
solution을작성하라.
단, divisor로 나누어 떨어지는 elment가 하나도 없다면
배열에 -1을 담아 반환하라.


'''

arr1 = [ [5,9,7,10], [2,36,1,3], [3,2,6]]
divisor1 = [5,1,10]


def solution(arr, divisor):
    answer = []

    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])

    if len(answer) == 0 : answer.append(-1)
    answer.sort()
    return answer


print(solution(arr1[0],divisor1[0]))
print(solution(arr1[1],divisor1[1]))
print(solution(arr1[2],divisor1[2]))

# 다른사람의 풀이
def solution2(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

'''
파이썬에서는, 앞에것이 거짓일 때 뒤에 것이 호출된다.
'''