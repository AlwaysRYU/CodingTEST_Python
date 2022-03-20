# 크레인 인형뽑기 게임
'''
https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
난이도 : 1
'''
'''
'''

# 류기탁 풀이

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

# 이중배열에서  len(리스트)는 행의 크기
# 위에선 5임

def solution(board, moves):
    answer = 0
    resultlist = []

    for i in moves:
        for j in range(len(board)):
            #5번 반복 
            if board[j][i-1] != 0 :
                if len(resultlist) < 1 :
                    resultlist.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
                else :
                    temp = resultlist.pop()
                    if temp == board[j][i-1] :
                        # 터질 경우
                        board[j][i-1] = 0
                        answer += 2
                        break
                    else :
                        resultlist.append(temp) #뺐던거 넣어주고
                        resultlist.append(board[j][i-1]) #이번것도 넣고
                        board[j][i-1] = 0
                        break  
                
    return answer

print(solution(board,moves))

# 다른 사람의풀이
def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
