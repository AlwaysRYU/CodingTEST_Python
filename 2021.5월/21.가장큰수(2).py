# 가장큰수
# https://programmers.co.kr/learn/courses/30/lessons/42746

# 두번째시도
# 저번실패의 이유 -> 시간초과 순열 사용하지말자.

'''
{40, 403}
{40, 405}
{40, 404}
{12, 121}
{2, 22, 223}
{21, 212}
{41, 415}
{2, 22}
{70, 0, 0, 0}
{0, 0, 0, 0}
{0, 0, 0, 1000}
{12, 1213}
'''
a = [2,22,223]
b = [41,415,465,532,44,3,5,7,88,9,123]
c = [0,0,0,1000]


def solution(numbers):
    answer = 0
    strlist = [str(i) for i in numbers]
    strlist.sort(key = lambda x : x[0] , reverse= True)
    print(strlist)

    return answer

def bikyo(str, listt):
    maxstr = ""
    listt.sort(key = lambda x : x[0], reverse=True)
    # 9부터 0까지
    # num = int(listt[0][0])
    templist = []

    for i in range(len(listt)):
        if int(listt[i][0]) == num :
            templist.append(listt[i])
            continue
        #이제 5이 아니면,
        else :
            bikyo(str(num),templist)
            templist = []
            num -= 1




    templist = []
    # while listt:
    #     while int(listt[0][0]) == num :
    #         #나누기 시작
    #         front = [] 
    #         middle = []
    #         last = []
    #         if len(listt[0]) >= 2:
    #             if int(listt[0][1]) > num :
    #                 front.append(listt[0])
    #                 del listt[0]
    #                 continue
    #             elif int(listt[0][1]) < num:
    #                 last.
                


    #     if int(listt[0]) == num and len(listt[0]) >= 2:
    #         if listt[1] >= num:

    #         templist.append(listt[0])
    #         del listt[0]
    #         continue
        
    #     maxstr += bikyo(str(num),templist)


    #     num -= 1


    return maxstr
        


bikyo(a)
    

print(solution([6,10,2]))
print(solution([30,3,34,5,9]))
# print(solution(a))
# print(solution(b))
# print(solution(c))