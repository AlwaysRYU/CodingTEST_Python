# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059


# 뭔가 처음에는 기가막힌 좋은 방법이 있을 줄 알았는데,
# 달리 방법이 없는 것같다.
# 전부 다해보는것 빼고

def rotate(array):
    N = len(array)
    rotateArr = [[0] * N for _ in range(N) ]
    # 행렬 생성하기
    print(rotateArr)
    for i in range(N) : 
        for j in range(N) : 
            rotateArr[i][j] = array[N-1-j][i]
    return rotateArr

def check(array):
    # lock 돌면서 됐는가 확인하기.


    return False

# print(rotate([[0, 0, 0], [1, 0, 0], [0, 1, 1]]))
print(rotate([[0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0],[0, 1, 1, 0]]))


def solution(key, lock):
    answer = False
    # N * N 배열 back  만들기
    # N 은 lock + 2(key -1)이다.

    # 그리고 for문돌면서 
    # lock 만큼 반복하기
    # 4번돌리고 체크하면서 맞으면 true출력한다.   

    return answer
