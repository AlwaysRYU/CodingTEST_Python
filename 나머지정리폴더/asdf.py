''' 

def solution(para):
    answer = ''
    total = 0
    dic = {"BOOL" : 1 , "SHORT" : 2, "FLOAT" : 4 , "INT" : 8, "LONG" : 16 }

    before = ""
    temp = ""
    last = 0

    for i in para :
        if i == "BOOL" :
            temp += "#"
            last = 8 - len(temp)
            if len(temp) == 8 :
                answer = answer + "," + temp
                temp = ""
                last = 8
            before = "BOOL"

        elif i == "SHORT" :
            if before == "BOOL" and len(temp) + 3 > 8 :
                for i in range(last) :
                    temp += "."
                answer = answer + "," + temp
                total += 8
                temp = "##"
            elif before == "BOOL" and len(temp) + 3 < 8 :
                temp += ".##"
                last = 8 - len(temp)
            elif len(temp) + 2 > 8 :
                for i in range(last) :
                    temp += "."
                answer = answer + "," + temp
                total = 8
                temp = "##"
                last = 8 -len(temp)
            else :
                temp += 
                



        elif i == "FLOAT" :

        elif i == "INT" :

        elif i == "LONG" :

        


    return answer

print(solution(["INT","INT","BOOL","SHORT","LONG"]))

'''