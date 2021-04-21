# 다트 게임
# 2021.04.21.
# https://programmers.co.kr/learn/courses/30/lessons/17682
'''
다트게임은 다트를 세차례 던져, 그합계로 실력을 겨룬다.
규칙은 다음과 같다.
1. 총 3번의 기회
2. 한 기회마다 점수는 0~10 점
3. S D T 의 영역이 존재한다. 각각 1제곱, 2제곱, 3제곱이다.
4. 옵션으로 
* : 이전 점수 2배
# : 해당점수 마이너스
5. * 는 처음에도 가능하다. 이 경우 이번 점수 2배
6. * 는 중첩이 가능하다. 이경우 4배이다.
7. * # 효과와 중첩이 가능하다. 그러면 -2배가된다.
8. S D T 영역은 하나만 존재.
9. * # 는 점수마다 둘중 하나만 존재한다. 없을 수도 있다.

입력 :
0~10의 정수와 SDT*#로 구성된 문자열이 입력될시 반환하는 함수를 작성하라.

'''



test1, test2, test3 = "1S2D*3T" , "1D2S#10S" , "1D2S0T"
def solution2(dartResult):
    answer = 0
    #10을 B로 치환
    dartResult = dartResult.replace('10', 'B')
    # number, SDT
    number = ['0','1','2','3','4','5','6','7','8','9','B']
    number2 = [0,1,2,3,4,5,6,7,8,9,'B']
    SDT = ['S', 'D', 'T']

    dartlist = list(dartResult)

    take = 1
    beforeScore = 0
    example = 0

    print('dartlist : ' + str(dartlist))
    for i in range(len(dartlist)):
        print(str(dartlist[i]) + ' 할 차례 ')
        print(' take 는 ' + str(take))
        
        

        #숫자를 가져옴
        if dartlist[i] in number :
            if dartlist[i] == 'B' :
                tempscore = 10
                take = 1
                print('확인한 숫자 : ' + str(tempscore))
                continue
            else :
                tempscore =  int(dartlist[i])
                take = 1
                print('확인한 숫자 : ' + str(tempscore))
                continue
        
        #바로전 S D 가 나왔을 때,
        if take == 2 :
            if dartlist[i] == '*':
                #곱하기가 나올경우
                answer += (2 * tempscore) + ( 2 * beforeScore )
                beforeScore = (2 * tempscore)
                take = 1
                continue
            if dartlist[i] == '#':
                # #이 나올경우
                answer += (-1) * tempscore
                beforeScore = (-1) * tempscore
                take = 1
                continue
            elif i == len(dartlist) -1 :
                answer += tempscore
            else :
                # 이전 SD가 나왔고, 숫자가 나왔을 때
                beforeScore = tempscore
                take = 1
                continue

        if dartlist[i] in SDT:
            if  dartlist[i] == 'D' :
                tempscore = tempscore ** 2
                take = 2
                print('확인한 글자 : ' + str(dartlist[i]))
                continue
            elif dartlist[i] == 'T' :
                tempscore = tempscore ** 3
                take = 2
                print('확인한 글자 : ' + str(dartlist[i]))
                continue
            else : 
                take = 2
                print('확인한 글자 : S')
                continue

        
    return answer 



def solution(dartResult):
    answer = 0
    templist = []

    tempstr = ""

    number = ['0','1','2','3','4','5','6','7','8','9']
    SDT = ['S', 'D', 'T']

    
    for i in range(len(dartResult)):
        print(str(i+1) + '번째 글자 : ' + str(dartResult[i]) )

        #마지막 글자일 경우 그냥 넣음
        if i == len(dartResult) -1 :
            print('마지막글자입니다.')
            tempstr += dartResult[i]
            templist.append(tempstr)
            break

        # 글자가 * # 의 경우 넣음
        elif dartResult[i] == '*' or dartResult[i] == '#' :
            tempstr += dartResult[i]
            templist.append(tempstr)
            tempstr =""
            continue

        # 숫자가 나왔는데 전에 글자가 SDT의 경우 넣음.
        elif dartResult[i] in SDT :
            # SDT 다음에 숫자일경우
            if dartResult[i+1] in number :
                tempstr += dartResult[i]
                templist.append(tempstr)
                tempstr =""
                continue
            #숫자가 아닐경우
            else : 
                tempstr += dartResult[i]
                continue 

        #아니면 넣음
        else : tempstr += dartResult[i]

    # templist로 나눴다.        
    print(templist)



    return answer

print(solution2(test1))
print(solution2(test2))
print(solution2(test3))