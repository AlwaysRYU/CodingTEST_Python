# 배달
#  https://programmers.co.kr/learn/courses/30/lessons/12978?language=python3
#

from collections import deque

def solution(N, road, K):
    answer = 0
    answerdict = {}
    answerdict[1] = 0
    # for i in range(1,N) :
    #     answerdict[i+1] = 'none'
    # print(answerdict)


    # 굳이 정렬?
    # road = sorted(road, key = lambda x : x[0])
    # finish = []
    # queue = deque()
    # print("지도정렬 : " + str(road))
    # while len(finish) < N :

    graph = {}
    #그래로 전환하기
    for i in range(len(road)):
        start = road[i][0]        
        end = road[i][1]
        length = road[i][2] 

        graph[start] = graph.get(start,[]) + [(end,length)]
        graph[end] = graph.get(end,[]) + [(start,length)]

    # 끝난 후
    print(graph)
    print(graph[1][0])
    abc = graph[1][0]
    print(abc[1])
    return answer



n1, r1, k1 = 5,	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 	3
n2, r2, k2 = 6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],	4

sorted(r1,key = lambda x : x[1])

print(solution(n1,r1,k1))
print(solution(n2,r2,k2))
