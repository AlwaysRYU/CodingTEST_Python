
S1 = "John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker"
C1 = "Example"

import re

def solution(S, C):
    answer = ""
    mail = C.lower()
    Seprate = S.split(", ")

    namelist = []
    reallist = []

    pat = re.compile("(\w{0,100})[-]\w{0,100}")

    # print(Seprate)
    for i in Seprate :
        Name = i.split(" ")
        if pat.match(Name[0]) :
            ex1, ex2 = Name[0].split("-")
            First = str(ex1) + str(ex2)
        else :
            First = Name[0]

        print(Name[-1])
        if pat.match(Name[-1]) :
            ex1, ex2 = Name[-1].split("-")
            print("매치")
            Second = ex1 + ex2    
        else :
            Second = Name[-1]

        temp = First.lower() + "." + Second.lower()

        if not temp in namelist :
            namelist.append(temp)
            reallist.append(temp)
        else :
            a = namelist.count(temp)
            namelist.append(temp)
            reallist.append(temp + str(a + 1))
        # text = "<" + Name[0].lower() + "." + Name[-1].lower() + "@" + mail + ".com>"
        # print(text)
    print(namelist)
    print(reallist)

    for i in range(len(reallist)) :
        # print(Seprate[i] + " <" + reallist[i] + "@" + mail + ".com>")
        answer += Seprate[i] + " <" + reallist[i] + "@" + mail + ".com>, "

    return answer[:-2]


print(solution(S1, C1))