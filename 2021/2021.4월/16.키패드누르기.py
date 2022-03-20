# 키패드 누르기
# 2021.04.14
'''
 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

'''

numberss = [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] ]
hands = ["right", "left", "right"]

#이게 진짜 류기탁 풀이
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


# 피드백 :
'''
유사한 부분은 새로 정의를 해서 코드길이를 줄일 수 있을 것..
'''


print(solution2(numberss[0], hands[0]))
print()
print(solution2(numberss[1], hands[1]))
print()
print(solution2(numberss[2], hands[2]))

#고민의 흔적
# def solution(numbers, hand):
#     answer = ''
#     Llv = 3
#     Rlv = 3

#     for i in range(len(numbers)):
#         if numbers[i] % 3 == 1 :
#             Llv = int(numbers[i] / 3)  #몫
#             Lmiddle = 0
#             answer += 'L'

#         elif numbers[i] % 3 == 0 :
#             Rlv = int(numbers[i] / 3)  #몫
#             Rmiddle = 0
#             answer += 'R'
#         else :
#             # 가운데 경우
#             if numbers[i] == 0 :
#                 temp = 3
#             else : 
#                 temp = int(numbers[i] / 3)  #몫
            
#             if Rmiddle == 1 :
#                 #만약 오른손이 가운데에 있다면,
#                 if abs(Rlv-temp) >= 2 and abs(Llv-temp) <= 1 :
#                     Lmiddle = 1 
#                     answer += 'L'
#                 else :
#                     Rmiddle = 1
#                     answer +='R'
            

                

#             if hand == 'right' :
#                 #오른손잡이의 경우 
#                 if (abs(Llv-temp) > abs(Rlv-temp)):
#                     Rlv = temp
#                     Rmiddle = 1
#                     answer += 'R'


#             if (abs(Llv-temp) == abs(Rlv-temp)):
#                 if hand == 'right' :
#                     Rlv = temp
#                     answer += 'R'
#                 else :
#                     Llv = temp
#                     answer += 'L'
#             elif (abs(Llv-temp) > abs(Rlv-temp)):
#                 #좌측 차이가 더 큰경우, 오른쪽으로 누름
#                 Rlv = temp
#                 answer += 'R'
#             else :
#                 Llv = temp
#                 answer += 'L'
        

#     return answer

#     # position = [[0,0,1], [0,1,2], [0,2,3],
#     # [1,0,4], [1,1,5], [1,2,6],
#     # [2,0,7], [2,1,8], [2,2,9],
#     # [3,0,-1], [3,1,0], [3,2,-1]]

# def solution2(numbers, hand):
#     answer = ""



#     L = [3,0]
#     R = [3,2]

#     #기본적으로 [목, 나머지]
#     for i in range(len(numbers)):
#         if numbers[i] % 3 == 1 :
#             L = [int(numbers[i] / 3) , 0]  #몫
#             answer += 'L'
#             print('왼손의 위치')
#             print(L)
#         elif numbers[i] % 3 == 0 :
#             R = [int(numbers[i] / 3) -1 , 2]  #몫
#             answer += 'R'
#             print('오른손의 위치')
#             print(R)
#         else :
#             # 가운데 경우
#             # 좌표설정
#             if numbers[i] == 0 :
#                 tempx = 3
#             else :
#                 tempx = int(numbers[i] / 3)
            
#             #거리비교
#             leftdistance = abs(L[0] - tempx) + abs(L[1] - 1)
#             rightdistance = abs(R[0] - tempx) + abs(R[1] - 1)

#             if leftdistance > rightdistance :
#                 # 왼손이 멀 경우, 오른손을 사용
#                 R = [tempx, 1]
#                 answer += 'R'
#                 print('오른손의 위치')
#                 print(R)
#             elif leftdistance < rightdistance :
#                 #오른손이 멀경우, 왼손을 사용
#                 L = [tempx, 1]
#                 answer += 'L'
#                 print('왼손의 위치')
#                 print(L)
#             else :
#                 if hand == 'right' :
#                     R = [tempx, 1]
#                     answer += 'R'
#                     print('오른손의 위치')
#                     print(R)
#                 else : 
#                     L = [tempx, 1]
#                     answer += 'L'
#                     print('왼손의 위치')
#                     print(L)
#     return answer