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
        j = 0
        for j in range(len(board)):
            #5번 반복 
            if board[i-1][j] != 0 :
                if len(resultlist) < 1 :
                    resultlist.append(board[i-1][j])
                    break
                else :
                    temp = resultlist.pop()
                    if temp == board[i-1][j] :
                        # 터질 경우
                        answer += 2
                        break
                    else :
                        resultlist.append(temp) #뺐던거 넣어주고
                        resultlist.append(board[i-1][j]) #이번것도 넣고
                        break  
                
    return answer

print(solution(board,moves))