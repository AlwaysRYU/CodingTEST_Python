# 문자열 내마음 대로 정하기 
# https://programmers.co.kr/learn/courses/30/lessons/12915

s, n = ["sun", "bed", "car"], 1
s2, n2 = ["abce", "abcd", "cdx"], 2


#2021.05.15.
def solution(string, n):
    answer = []
    # cut = [[],[]]
    # dicti = {}

    # for i in string:
    #     cut[0].append(i[n:])
    #     cut[1].append(i)

    answer = sorted(string, key = lambda x : (x[n],x[:n]))
    return answer


print(solution(s,n))
print(solution(s2,n2))
s3 = ["sun","aun","xun","ee"]
print(solution(s3,1))

# 지난 것
'''
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

'''
#딕셔너리 사용은 중복때문에 안되겠다
'''

def solution(string, n):
    answer = []
    cut = []
    dicti = {}

    for i in string:
        cut.append(i[n:])
        #dicti[키] = 값
        dicti[i[n:]] = i

    cut.sort()
    for i in range(len(cut)):
        answer.append(dicti[cut[i]])
    print(cut)
    print(dicti)
    return answer
'''