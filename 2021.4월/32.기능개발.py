# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
'''
'''
p = [93, 30, 55]	
s = [1, 30, 5]
p2 = [95, 90, 99, 99, 80, 99]	
s2 = [1, 1, 1, 1, 1, 1]
p3 = [40,93,30,55,60,65]
s3 = [60,1,30,5,10,7]
p4 = [93,30,55,60,40,65]
s4 = [1,30,5,10,60,7]
def solution(P, S):
    answer = []
    
    timelist = []

    for i in range(len(P)):
        temp = ( 100 - P[i] ) // S[i]
        if ( 100 - P[i] ) % S[i] > 0 :
            timelist.append(temp + 1)
        else :
            timelist.append(temp)
    print()
    print(timelist)

    a = 0
    maxday = 0
    for j in range(len(timelist)):
        if j == 0 : 
            maxday = timelist[j]
            a += 1
            continue

        if timelist[j] > maxday :
            maxday = timelist[j]
            answer.append(a)
            a = 1
        else : a += 1
    
    answer.append(a)
    return answer


print(solution(p,s))
print(solution(p2,s2))
print(solution(p3,s3))
print(solution(p4,s4))

# 다른사람의 풀이
def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        # 큐의 길이가0이거나 
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
# 학습 : zip
# 

'''
releaseL = [1]
    for j in range(1, len(timelist)):
        if timelist[j-1] >= timelist[j]:
            releaseL.append(-1)
        else:
            releaseL.append(+1)

    print(releaseL)

    release = 1
    for k in range(1,len(releaseL)):
        if k == 1:
           if releaseL[k] == -1:
               release +=1
               continue
           else : 
               answer.append(release)
               continue

           
        if releaseL[k-1] == -1 and releaseL[k] == 1 :
            answer.append(release)
            release = 1
        else:
            release +=1

    answer.append(release)
'''