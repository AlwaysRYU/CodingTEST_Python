# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257


import itertools

# # 3P2
# arr = ['A', 'B', 'C']
# nPr = list(itertools.permutations(arr,2))

def calculate(number1,cal,number2):
    if cal == "*":
        return float(number1) * float(number2)
    elif cal == "+":
        return float(number1) + float(number2)
    elif cal == "-":
        return float(number1) - float(number2)

def solution(expression):
    answer = 0
    
    yun = ["+","-","*"]
    #파이썬 절대값
    #abs(-32)
    split = []
    yeon = list(itertools.permutations(yun,3))
    print("연산자 목록 : ")
    print(yeon)

    j = 0
    i = 0
    for i in range(len(expression)):
        if len(expression)-1 == i :
            split.append(expression[j:])
        if expression[i] in yun:
            split.append(expression[j:i])
            split.append(expression[i])
            j = i + 1
    print(split)
    print()


    print("---<계산시작>---")
    for i in range(len(yeon)):
        #똑같은 임시리스트 
        templist = split
        print("split : " + str(split))
        print("복사함" + str(templist))
        # 1 3 5 는 연산자임
        print("이번 우선 순위 : " + str(yeon[i]))
        for k in range(len(yeon[i])):
            j = 1 # 복사한 templist 의 1부터 홀수로 돈다.
            print("이번연산자 : " + str(yeon[i][k]))  
            while True :   
                # 만약 넘으면, 마지막 연산자라면 바로 탈출
                if len(templist) == 1:
                    break
                if j >= len(templist) -2:
                    if yeon[i][k] == templist[-2] :
                        
                        temp = calculate(templist[j-1],templist[j],templist[j+1])
                        del templist[j-1]
                        del templist[j-1]
                        templist[j-1] = str(temp)
                        print(str(yeon[i][k]) + "계산함")
                        print(templist)
                        j = 1
                    break

                if yeon[i][k] == templist[j] :
                    print(str(yeon[i][k]) + "계산함")
                    temp = calculate(templist[j-1],templist[j],templist[j+1])
                    del templist[j-1]
                    del templist[j-1]
                    templist[j-1] = str(temp)
                    print(templist)
                    j = 1
                j += 2
            
            if len(templist) == 1 :
                print(templist)
                print("연산자의 순서 " + str(yeon[i]))
                print("결과 " + str(result))
                if abs(result) > abs(answer):
                    answer = result 
                break
            elif len(templist) == 3 :
                result = calculate(templist[0],templist[1],templist[2])
                print(templist)
                print("연산자의 순서 " + str(yeon[i]))
                print("결과 " + str(result))
                if abs(result) > abs(answer):
                    answer = result 
                break
        print("우선순위 끝 ------")
        print()

    
    return answer



print(solution("100-200*300-500+20"))
#print(solution("50*6-3*2"))