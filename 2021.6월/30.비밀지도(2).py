# 비밀 지도
# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3

n1 = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

n2 = 6
arrr1 = [46, 33, 33 ,22, 31, 50]
arrr2 = [27 ,56, 19, 14, 14, 10]

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        print(i+1)
        print(bin(arr1[i]))
        print(bin(arr2[i]))
        print('OR연산')
        print(bin(arr1[i] | arr2[i])[2:])
        text = bin(arr1[i] | arr2[i])[2:]
        while len(text) < n :
            text = "0" + text
        tempstr = ["#"] * n

        for j in range(n) :
            if text[j] == "0" :
                tempstr[j] = " "
        answer.append("".join(tempstr))

    return answer

# print(solution(n1,arr1,arr2))
print(solution(n2,arrr1, arrr2))

# 다른사람의 풀이2
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

# 정리해놓은게 있지만, 기억하지 못했다. 다음에 풀때는 생각해보자.