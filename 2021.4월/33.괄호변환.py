# 괄호변환
# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
# 2021.04.30.
# 주제 : 2020 카카오 블라인드 리크루트먼트
'''

'''
pp = "(()())()"
pp2 =")("
pp3 ="()))((()"

def B(p):
        M = 0
        for i in range(len(p)):
            if p[i] == '(': M += 1
            elif p[i] == ')' : M -= 1
            
            if M == 0 : return p[:i+1], p[i+1:]

def All(p):
        M = 0
        for i in range(len(p)):
            if p[i] == '(': M += 1
            elif p[i] == ')' : M -= 1

            if M < 0:
                # print("올바른 괄호 문자열이 아닙니다.")
                return False

            if i == len(p)-1 and M == 0 : return True
            #올바른 문자열일 경우 True를 반환


def solution2(p):
    answer = ""
    print( p + " 정렬을 시작합니다.")
    # 1. 입력이 빈 문자열일 경우, 빈 문자열을 반환한다.
    if p == "" : 
        print("이 문자열은 비었습니다.")
        return p
    
    # 2. 문자열을 두 균형잡힌 문자열 U V 로 분리한다.
    # 단 U는 균형잡힌 괄호 문자열로 더이상 분리할수 없다.
    # V는 빈문자열이 될수 있다.
    u , v = B(p)
    print(" u : " + u)
    print(" v : "  + v)

    # 3. 문자열 U가 올바른 문자열 이라면,
    # 문자열 v에대해 1단계부터 다시수행한다.
    if All(u) == True :
        # 3-1 수행한 결과 문자열을 u에 이어 붙인 후 반환한다.
        print(u + " 는 올바른 문자열입니다.")
        return u +solution2(v)
    elif All(u) == False:
        print(u + " 는 올바른 문자열이 아닙니다.")
        # 4. 문자열 u가 올바른 문자열이 아니라면,
        # 4-1. 빈문자열에 첫번째 문자로 "("를 붙인다.
        temp ="("
        # 4-2 문자열 v에 대해 1단계부터 재귀적으로 수행환 결과문자열을 이어붙인다.
        temp += solution2(v)
        # 4-3. ")"를 다시 붙인다.
        temp += ")"
        # 4-4. u의 첫번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호방향을 뒤집어서 뒤에 붙인다.
        
        A = list(u)
        del A[0]
        del A[-1]
        print(str(A) + " A 는 이렇습니다.")
        newstr = ''.join(A)
        j = newstr.replace('(','-')
        jj = j.replace(')','(')
        jjj = jj.replace('-',')')
        print(jjj + "바뀌었습니다.")
        temp += jjj
        # 4-5. 생성된 문자열을 반환한다.
        return temp
    
    return answer 


# print(solution2(pp))
# print(solution2(pp2))
print(solution2(pp3))

# 다른 사람의 풀이
def solution3(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution3(p[i+1:])
            else:
                # 이게 포인트네
                # p[1:i]로 맨앞 뒤 글자 하나씩 제거하고  lmabda로 ( ) 교체해보리기
                return '('+solution3(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))



# 고뇌의 흔적
# def solution(p):
    
#     def All(p):
#         M = 0
#         for i in range(len(p)):
#             if p[i] == '(': M += 1
#             elif p[i] == ')' : M -= 1

#             if M < 0:
#                 print("올바른 괄호 문자열이 아닙니다.")
#                 return False

#             if i == len(p)-1 and M == 0 : return True
#             #올바른 문자열일 경우 True를 반환
    
#     def B(p):
#         M = 0
#         for i in range(len(p)):
#             if p[i] == '(': M += 1
#             elif p[i] == ')' : M -= 1
            
#             if M == 0 : return p[:i+1], p[i+1:]
    
#     if p == "" : return p
#     u , v = B(p)
#     if All(u) == True :
#         B(v)
#         answer = answer + u
    



#     answer = ''
#     return answer
