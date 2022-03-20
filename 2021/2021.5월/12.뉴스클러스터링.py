# 뉴스클러스터링
#


s1, t1 = 'FRANCE',	'french' #16384
s2, t2 = 'handshake',	'shake hands'	#65536
s3, t3 = 'aa1+aa2',	'AAAA12'	#43690
s4, t4 = 'E=M*C^2',	'e=m*c^2' 

import re

#나의 풀이
def solution(str1, str2):
    answer = 0
    # str1 = re.sub("[^a-zA-Z]","",str1)
    # str2 = re.sub("[^a-zA-Z]","",str2)
    print(str1)
    print(str2)
    da1 = []
    da2 = []
    
    p = re.compile('[a-zA-Z]')
    
    temp = str1[0]
    for i in range(1,len(str1)):
        if p.match(str1[i]):
            temp += str1[i]
            if len(temp) >= 3 :
                temp = temp[1:]
        else :
            temp = ""
            continue

        if len(temp) == 2 :
            print("특수문자가 없음")
            da1.append(temp.upper())
        #print(str1[i:i+2])
    
    da1.sort()
    print("집합 1: ")    
    print(da1)
    
    temp = str2[0]
    for i in range(1,len(str2)):
        if p.match(str2[i]):
            temp += str2[i]
            if len(temp) >= 3 :
                temp = temp[1:]
        else :
            temp = ""
            continue

        if len(temp) == 2 :
            print("특수문자가 없음")
            da2.append(temp.upper())    
        #print(str1[i:i+2])

    da2.sort()    
    print("집합 2: ") 
    print(da2)
    
    if len(da1) + len(da2) == 0 :
        return 65536
    
    kyo = []
    hap = []
    for i in range(len(da1)):
        if da1[i] in da2:
            # 있으면 (교집합이면)
            kyo.append(da1[0])
            da2[da2.index(da1[i])] = -2
            da1[i] = -1

            hap.append(da1[0])

        else:
            hap.append(da1[0])
    
    for i in range(len(da2)):
        if da2[i] == -2 :
            continue
        if not da2[i] in da1 :
            hap.append(da2[i])

    print(kyo)
    print(hap)
    a = len(kyo)/len(hap)
    print(a)
    answer = int(a * 65536)
    
    return answer

print(solution(s1,t1))
print(solution(s2,t2))
print(solution(s3,t3))
print(solution(s4,t4))



import re
import math

#다른사람의 풀이
def solution2(str1, str2):
    # 소문자로 바꾸고 
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    #이게 포인트네..
    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

'''

def solution(str1, str2):
    answer = 0
    # str1 = re.sub("[^a-zA-Z]","",str1)
    # str2 = re.sub("[^a-zA-Z]","",str2)
    print(str1)
    print(str2)
    da1 = set([])
    da2 = set([])
    
    p = re.compile('[a-zA-Z]')
    
    temp = str1[0]
    for i in range(1,len(str1)):
        if p.match(str1[i]):
            temp += str1[i]
            if len(temp) >= 3 :
                temp = temp[1:]
        else :
            temp = ""
            continue

        if len(temp) == 2 :
            print("특수문자가 없음")
            da1.add(temp.upper())
        #print(str1[i:i+2])
        
    print("집합 1: ")    
    print(da1)
    
    temp = str2[0]
    for i in range(1,len(str2)):
        if p.match(str2[i]):
            temp += str2[i]
            if len(temp) >= 3 :
                temp = temp[1:]
        else :
            temp = ""
            continue

        if len(temp) == 2 :
            print("특수문자가 없음")
            da2.add(temp.upper())    
        #print(str1[i:i+2])

    
    print("집합 2: ") 
    print(da2)
    
    if len(da1) + len(da2) == 0 :
        return 65536
    
    kyo = da1.intersection(da2)
    hap = da1.union(da2)
    print(kyo)
    print(hap)

    a = len(kyo)/len(hap)
    print(a)
    answer = int(a * 65536)


    return answer

print(solution(s1,t1))
print(solution(s2,t2))
print(solution(s3,t3))
print(solution(s4,t4))
'''