s, n = ["sun", "bed", "car"], 1
s2, n2 = ["abce", "abcd", "cdx"], 2

def solution(string, n):
    answer = []
    temp = [[0 for _ in range(3)] for _ in range(len(string))]
    print(temp)
    for i in range(len(string)):
       temp[i][1] = i
       temp[i][0] = string[i][n]
       temp[i][2] = string[i]

    temp.sort()
    for i in range(len(string)):
        answer.append(temp[i][2])
    print(temp)
    return answer


def solution2(string, n):
    answer = []
    
    for i in range(len(string)):
        


    return answer


print(solution(s,n))
print(solution(s2,n2))