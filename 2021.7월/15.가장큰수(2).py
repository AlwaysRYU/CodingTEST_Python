# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746



# 방법1 
# 조합으로 모두 만들어서 하는것.
# 당연히 시간 초과 뜨겠지.
import itertools
def solution(arr) :
    answer = ""
    templist = []
    for i in arr :
        templist.append(str(i))

    Plist = list(map(''.join, itertools.permutations(templist)))
    print(Plist)
    maxx = int(Plist[0])
    for i in range(1,len(Plist)):
        if int(Plist[i]) > maxx :
            maxx = int(Plist[i])
    return str(maxx)

print(solution([6,10,2]))
print(solution([3,30,34,5,9]))

# 방법2
# 참신한 방법!!! 내일 풀어봐라..