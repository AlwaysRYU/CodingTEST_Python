# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3


s1, s2, s3, s4, s5 = "{{2},{2,1},{2,1,3},{2,1,3,4}}", "{{1,2,3},{2,1},{1,2,4,3},{2}}", "{{20,111},{111}}", "{{123}}" , "{{4,2,3},{3},{2,3,4,1},{2,3}}"

def solution(s):
    print(s)
    arr = s[2:-2].split("},{")
    print(arr)
    # 지금은 str
    arr2 = []
    dic = {}

    for i in range(len(arr)):
        arr2.append(arr[i].split(','))
        dic[len(arr2[i])] = arr[i].split(',')
    print(arr2)
    print(dic)

    answer = []
    for i in range(1, len(arr2)+1):
        templist = dic[i]
        for j in range(len(templist)):
            if not int(templist[j]) in answer :
                answer.append(int(templist[j]))
    return answer

print(solution(s1))
print(solution(s2))
print(solution(s3))
# print(solution(s4))
# print(solution(s5))

# 다른 사람의 풀이
def solution2(s):
    # Counter : 길이 수를 세기
    s = Counter(re.findall('\d+', s))
    # a.items() : key value 쌍 을 얻는다.
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter

#다른사람들 나와 유사하다.
def solution3(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer