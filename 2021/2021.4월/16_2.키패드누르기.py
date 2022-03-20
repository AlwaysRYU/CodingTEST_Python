
numberss = [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] ]
hands = ["right", "left", "right"]

def solution2(numbers, hand):
    answer = ""
    L = [3,0]
    R = [3,2]

    for i in range(len(numbers)):
        if numbers[i] == 0:
            tempx = 3
            leftdistance = abs(L[0] - tempx) + abs(L[1] - 1)
            rightdistance = abs(R[0] - tempx) + abs(R[1] - 1)
            if leftdistance > rightdistance :
                # 왼손이 멀 경우, 오른손을 사용
                R = [tempx, 1]
                answer += 'R'
                print('오른손의 위치')
                print(R)
                continue
            elif leftdistance < rightdistance :
                #오른손이 멀경우, 왼손을 사용
                L = [tempx, 1]
                answer += 'L'
                print('왼손의 위치')
                print(L)
                continue
            else :
                if hand == 'right' :
                    R = [tempx, 1]
                    answer += 'R'
                    print('오른손의 위치')
                    print(R)
                    continue
                else : 
                    L = [tempx, 1]
                    answer += 'L'
                    print('왼손의 위치')
                    print(L)
                    continue


        if numbers[i] % 3 == 2:
            tempx = int(numbers[i] / 3)
            #거리비교
            leftdistance = abs(L[0] - tempx) + abs(L[1] - 1)
            rightdistance = abs(R[0] - tempx) + abs(R[1] - 1)

            if leftdistance > rightdistance :
                # 왼손이 멀 경우, 오른손을 사용
                R = [tempx, 1]
                answer += 'R'
                print('오른손의 위치')
                print(R)
            elif leftdistance < rightdistance :
                #오른손이 멀경우, 왼손을 사용
                L = [tempx, 1]
                answer += 'L'
                print('왼손의 위치')
                print(L)
            else :
                if hand == 'right' :
                    R = [tempx, 1]
                    answer += 'R'
                    print('오른손의 위치')
                    print(R)
                else : 
                    L = [tempx, 1]
                    answer += 'L'
                    print('왼손의 위치')
                    print(L)

        elif numbers[i] % 3 == 1:
            L = [int(numbers[i] / 3) , 0]  #몫
            answer += 'L'
            print('왼손의 위치')
            print(L)

        else :
            R = [int(numbers[i] / 3) -1 , 2]  #몫
            answer += 'R'
            print('오른손의 위치')
            print(R)

    return answer 




print(solution2(numberss[0], hands[0]))
print()
print(solution2(numberss[1], hands[1]))
print()
print(solution2(numberss[2], hands[2]))
