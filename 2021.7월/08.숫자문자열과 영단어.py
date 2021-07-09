# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301

# 나의풀이
def solution(s):
    number = (len(s) // 3)
    s = s.replace('zero', '0', number)
    s = s.replace('one', '1', number)
    s = s.replace('two', '2', number)
    s = s.replace('three', '3', number)
    s = s.replace('four', '4', number)
    s = s.replace('five', '5', number)
    s = s.replace('six', '6', number)
    s = s.replace('seven', '7', number)
    s = s.replace('eight', '8', number)
    s = s.replace('nine', '9', number)
    return int(s)
# 굳이 횟수 안하더라도 replace는 전부 바꿔준다.

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution2(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
print(solution2("ninenineninenine"))


# 다른 사람의 풀이