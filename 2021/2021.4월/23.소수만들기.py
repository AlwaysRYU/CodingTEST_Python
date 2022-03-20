# 소수 만들기
# 2021.04.20
# https://programmers.co.kr/learn/courses/30/lessons/12977

'''
주어진 숫자 중 3개를 더했을 때, 소수가 되는 경우의 개수를 구하라.


'''

test1, test2 = [1,2,3,4], [1,2,7,6,4]

import itertools

def solution(nums):
    answer = 0

    numbers = list(itertools.combinations(nums,3))
    print('총 숫자 조합 수 ')
    print(numbers)

    for i, j, k in numbers :
        hap = i + j + k
        print('이번 합은' + str(hap))
        nanugi = hap -1

        while nanugi > 1 :
            if (hap % nanugi) == 0 :
                break
            elif nanugi == 2 and (hap % nanugi) != 0:
                answer += 1
            nanugi -= 1 
        
    return answer

print(solution(test1))
print(solution(test2))