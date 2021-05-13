# 후보키
# 

r1 = [["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]]

import itertools
# 조합

# 중복이 없으면 무조건 후보키 가능.
# 유일성 -> 어떠한 키로 행을 바로 찾아낼 수 있는  기능
def solution(relation):
    answer = 0
    unique = []
    minimal = []
    
    after = relation
    print(relation)

    # 유일성 판별
    for j in range(len(relation[0])):
        temp = []
        n = 0
        nn = len(relation)
        print(nn)

        for i in range(len(relation)):
            if not relation[i][j] in temp :
                temp.append(relation[i][j])
                n += 1
        
        if n == nn:
            answer += 1
            print(j)
            print("열은 중복이 없다.")
            unique.append(j)

        else :
            print(j)
            print("열은 중복이 있다.")

    after2 = []
    for i in range(len(unique)):
        for j in range(len(relation)):
            del after[j][i]
    print(after) # 중복이 있는 데이터

    # after2.append(list(itertools.combinations(after[i],i)))
    # nCr = list(itertools.combinations(arr,2))
    # print(nCr)
    return answer

# 다른사람의 풀이
from collections import deque
from itertools import combinations

'''
조합 까지는 접근 성공함, 하지만 큐를 써야하나.
'''

def solution2(relation):
    n_row = len(relation)
    n_col = len(relation[0])  

    candidates=[]
    #이게 내가 하고싶던거였는데.
    for i in range(1,n_col+1):
        candidates.extend(combinations(range(n_col),i))

    final=[]
    for keys in candidates:
        tmp=[tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp))==n_row:
            final.append(keys)
            
    # final : 가능한 모든 경우의 수에서 유일성을 만족하는 지 확인 
    # 튜플 형태로 해당하는 값을 추출해서 길이가 맞는 지 확인합니다. 
    # 예) (100, 200, ... , 600) 은 길이가 6으로 유일성 만족 

    answer=set(final[:])
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(final[i])==len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
                
    return len(answer)


print(solution(r1))