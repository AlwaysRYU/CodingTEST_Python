# 부품찾기
# 실전문제2 : P.197
'''
가게에 부품이 N개 있다.
손님이 M개 종류의 부품을 대량으로 구매한다.
가게안에 부품이 있는지 확인하는 프로그램을 작성한다.
손님이 찾는 것이 있다면 yes, 없다면 no 를 출력한다.
'''

G = [8,3,7,9,2]
F = [5,7,9]

def solution(Find, Jaego):
    
    for i in Find:
        if i in Jaego :
            print("yes",end= " ")
        else:
            print("no",end=" ")


solution(F,G)


# 떡볶이 떡 만들기
# 실전문제3 : P201
'''
높이 H를 지정하면 줄지어진 떡을 한번에 절단한다.
높이가 H보다 긴 떡은 잘리고, 짧은 떡은 잘리지 않는다.
잘린 부분을 손님이 가져간다.
그렇다면, 손님이 요청한 총길이가 M 일때, M만큼의 떡을 얻기위해 절단할 수 있는 높이의 최대값을 구하는프로그램을 작성하라.
ex, 
떡의 개수 -> 4
요청한 떡의길이 -> 6
떡 -> 19 15 10 17
출력 : 15 (15만큼 자르면 4 2 로 6을 가져갈 수 있다.)
'''
print()

# 나의풀이
def solution2(length, ddocklist):
    
    ddocklist.sort(reverse=True)
    print(ddocklist)
    answer = ddocklist[0]
    while True :
        temp = 0
        print("answer : " + str(answer))
        for i in range(len(ddocklist)):
            if ddocklist[i] >= answer :
                temp += (ddocklist[i] - answer)
        print("temp : " + str(temp))
        if temp >= length :
            return answer
        elif answer <= 0 :
            break
        else:
            answer -= 1
            continue
    return answer


solution2(6,[19,15,10,17])

