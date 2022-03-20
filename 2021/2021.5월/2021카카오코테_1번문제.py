def solution(s):
    answer = 0

    dicts2 = ["zero", "one", "two" ,"three", "four", "five", "six", "seven", "eight", "nine"]
    number = ["0","1","2","3","4","5","6","7","8","9"]
    
    ansstr = ""
    strr = ""
    while s:
        print(s)
        if s[0] not in number:
            strr += s[0]
            s = s[1:]
            if strr in dicts2 :
                print("들어감")
                ansstr += str(dicts2.index(strr))
                strr = ""
        elif s[0] in number :
            print("숫자임")
            ansstr += s[0]
            s = s[1:]

    answer = int(ansstr)
    return answer

    
print(solution("one4seveneight"))
