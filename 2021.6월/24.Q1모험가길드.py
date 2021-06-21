# Q-01 모험가 길드
'''
숫자가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참가해야한다.
출력 : 최대 몇 개의 모험가 그룹을 만들 수 있는지?
단, 모두 사용 안해도 된다.
'''

array = [2,3,1,2,2]

'''
모두 사용 안해도 되는 것이 포인트.
만들 수 있는 그룹의 최대 값 = 최소 인원으로 그룹을 만든다. 
이 것을 떠올려야한다.
'''


def solution(A):
    answer = 0
    A.sort()
    print(A)
    count = 0
    for i in A :
        count += 1
        if count >= i :
            answer += 1
            count = 0
    return answer

print(solution(array))
