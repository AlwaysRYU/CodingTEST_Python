# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3

# COPY CODE
def possible(answer) :
    for x, y, stuff  in answer :
        if stuff == 0 : # 설치된 것이 기둥일 때
            # 1 - 바닥위 or 보의 한쪽 끝 부분 위 or 다른 기둥 위라면 가능
            if y ==0 or ( [x-1,y,1] in answer ) or [x,y,1] in answer or [x,y-1,0] in answer :
                continue
            return False # 아니라면 거짓 반환

        elif stuff == 1 : # 설치된 것이 보일 경우
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1, y, 1] in answer)  :
            # 2 한쪽 끝 부분이 기둥위  혹은 양쪽 끝부분이 다른 보와 동시에 연결    
                continue
            return False
    return True

def solution(n, build_frame):
    answer = [] # answer은 기둥과 보의 리스트
    
    for frame in build_frame : # 조건 : 최대 1000개
        x,y,stuff,operate = frame 
        if operate == 0 :  # 0 일경우 삭제
            answer.remove([x,y,stuff]) # 일단 삭제를 하고
            if not possible(answer): # 가능한 구조물인가?
                answer.append([x,y,stuff]) # 가능한 구조물이 아니라면 '설치'
        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer): # 가능한 구조물인가?
                answer.remove([x,y,stuff]) # 가능한 구조물이 아니라면 '제거'
    
    return sorted(answer) # 정렬 후 리턴