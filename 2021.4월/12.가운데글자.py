# 가운데글자
# 2021.04.13.
# level 1
'''
https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3
단어s의 가운데 글자를 반환하는 함수를 만들어라.
짝수라면, 가운데 두글자를 반환하면된다.

'''

ss1, ss2 = "abcde", "qwer"

def solution(s):
    anslist = []

    templist = list(s)
    print(templist)
    print("문자열의 길이 " + str(len(templist)))

    if len(templist) % 2 == 0 :
        # 짝수 일경우
        anslist.append(templist[int(len(templist)//2)-1])
        anslist.append(templist[int(len(templist)//2)])
    else :
        anslist.append(templist[int(len(templist)//2)])

    
    print(anslist)
    answer = "".join(anslist)

    return answer

print(solution(ss1))
print(solution(ss2))

#다른 사람의 풀이
def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1) // 2 : len(str) // 2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))


