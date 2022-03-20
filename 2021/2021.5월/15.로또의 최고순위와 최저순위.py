# 로또의 최고순위와 최저순위
# https://programmers.co.kr/learn/courses/30/lessons/77484


l1, win1 = [44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]
l2, win2 = [0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25]
l3, win3 = [45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]

def solution(lottos, win_nums):
    answer = []
    least, maxx = 0, 0
    zero = 0
    for i in range(len(lottos)):
        if lottos[i] == 0 :
            zero += 1
            continue
        if lottos[i] in win_nums :
            least += 1
    maxx = zero + least
    #최고 먼저
    if maxx in [0,1]:
        answer.append(6)
    else :
        answer.append(7-maxx)
    
    if least in [0,1]:
        answer.append(6)
    else:
        answer.append(7-least)

    return answer

print(solution(l1,win1))
print(solution(l2,win2))
print(solution(l3,win3))


# 다른 사람의 풀이
def solution2(lottos, win_nums):

    #랭크 리스트
    
    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
#깔끔하다.
'''
    if least in [0,1] :
        answer.append(6)
        if zero in [0,1] :
            answer.append(6)
        else :
            answer.append(7 - zero)
    else :
        answer.append(7- least)
        if zero in [0,1] :
            answer.append(7-least)
        else :
            answer.append(7 - (least + zero))
    answer[0],answer[1] = answer[1], answer[0]
    
'''