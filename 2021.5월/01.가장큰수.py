# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
# 문제 타입 : 정렬
'''

'''
a1, a2 = [6, 10, 2], [3, 30, 34, 5, 9]

# 순열조합 사용시 임포트
import itertools

# 다른사람
def solution(num): 
    num = list(map(str, num)) 
    num.sort(key = lambda x : x*3, reverse = True) 
    return str(int(''.join(num)))


#시간초과,,, 다 시간초과 나오네 아무래도 일일히 하는것 힘든듯
def solution(numbers):
    maxx = 0
    
    Plist = list(itertools.permutations(numbers,len(numbers)))

    for i in range(len(Plist)):
        temp = ""
        for j in range(len(Plist[i])):
            temp = temp + str(Plist[i][j])
        if int(temp) > maxx :
            maxx = int(temp)
    answer = str(maxx)
    return answer

def solution2(numbers):
    answer = ""
    # numbers.sort(reverse=True)
    i = 0
    ten = 1
    N = 9
    numbers.sort()
    print(numbers)
    while True:
        print("제일 처음의 수 " + str(numbers[i]))
        if numbers[i] >= 10 :
            ten *= 10
        if numbers[i] < ten and str(numbers[i])[0] == str(N) :
            answer += str(numbers[i])
            print("현재" + answer)
            del numbers[i]
            if len(numbers) == 0 : break
            continue
        else:

        i += 1
        if  i == len(numbers): i =0
        N -= 1
        if N == 0: N = 9

    return answer

def solution3(numbers):
    answer = ''
    numbers.sort()

    T = 10
    temp = []
    while True:
        if numbers[0] < T : 
            temp.append(numbers[i])
            del numbers[0] 
            continue
        else 

    return answer
print(solution2(a1))
# print(solution2(a2))
