# 문자열 뒤집기

# 문자열 S는 0,1로 이루어졌다.
# 문자열 S의 모든 숫자를 전부 같게 만들려고 한다.
# 문자열 S에서, 연속된 하나 이상의 숫자를 잡고 모두 뒤집을 수 있다.

# ex 0001100 -> 1110011 -> 1111111  or 바로 0000000
# 출력 : 1

S1 = "0001100"

# 나의 풀이
def solution(S):
    answer0, answer1 = 0,0
    leng0, leng1 = 0,0
    for i in range(len(S)):
        if S[i] == "0" and leng1 >= 1:
            # 0이 되고, 1의 길이가 1이상일때 1을 0으로 교체 하고
            answer0 += 1
            leng1 = 0
        elif S[i] == "1":
            leng1 += 1
        if S[i] == "1" and leng0 >= 1:
            # 1이 되고, 0의 길이가 1이상일때 0을 1으로 교체 하고
            answer1 += 1
            leng0 = 0
        elif S[i] == "0":
            leng0 += 1
        
        if len(S)-1 == i :
            if leng1 != 0 :
                answer0 += 1
            if leng0 != 0 :
                answer1 += 1

    print(answer1)
    print(answer0)
    return min(answer1,answer0)

print(solution(S1))

# 풀이
'''
나와 같다. 
전부 0으로 바꾸는 경우와, 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산한다.
횟수를 세는 방법은 내가 첫번째 썼던 방법과 유사하다.
'''