# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

abc = ["119", "97674223", "1195524421"]
abc2 = ["123","456","789"]
abc3 = ["12","123","1235","567","88"]

def solution(phone):
    answer = True

    for i in phone :
        leng = len(i)
        for j in phone :
            if j != i and j[:leng] == i :
                return False
    return answer
#시간 초과가 뜬다. 테스트케이스는 다 통과했지만

def solution2(phone):
    answer = True
    length = len(phone)
    phone.sort(key = len)
    for i in range(length) :
        for j in range(i+1,length):
            if phone[j][:len(phone[i])] == phone[i] :
                return False
    return answer
# 조금 줄었지만 그래도 시간초과가 뜬다.
# sort 사용 / 이중 for 문이 문제의 원인이라고 생각한다.

def solution3(phone):
    answer = True
    phone.sort()

    for i in range(len(phone)-1):
        if phone[i] in phone[i+1]:
            return False
    return answer

print(solution2(abc))
print(solution2(abc2))
print(solution2(abc3))