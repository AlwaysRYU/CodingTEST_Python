# 파일명 정렬
# https://programmers.co.kr/learn/courses/30/lessons/17686?language=python3

strr = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
strr2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
strr3 = ["abc", "Abc", "ABC","aVC" ]

import re

def bigyo(A,B):
    before, nextt = "", "" 
    alpha = re.compile('[A-Za-z]')
    number = re.compile('[0-9]')
    HA , HB = "", ""
    BA , BB = "", ""
    
    # 일단 문자열로 먼저
    for i in range(len(A)):
        if number.match(A[i]) :
            HA = A[:i]
            for j in range(i,len(A)):
                if not number.match(A[j]):
                    BA = A[i:j]
                    break
                elif len(A[i:j]) == 5 :
                    BA = A[i:j]
                    break
            break

    for i in range(len(B)):
        if number.match(B[i]):
            HB = B[:i]
            for j in range(i,len(B)):
                if not number.match(B[j]):
                    BB = B[i:j]
                    break      
                elif len(B[i:j]) == 5 :
                    BB = B[i:j]
                    break
                
            break
    
    if HA.upper() == HB.upper() and int(BA) == int(BB) :
        return A, B
    elif HA.upper() != HB.upper() :
        templist = [A, B]
        templist.sort()
        return templist[0], templist[1]
    elif HA.upper() == HB.upper() :
        if int(BA) > int(BB) :
            return B, A
        else :
            return A, B
    return A, B

# print(bigyo("foo14.txt", "fad13.txt"))

def solution(files):
    if len(files) == 2:
        strr1, strr2 = bigyo(files[0], files[1])
        return [strr1, strr2]
    for i in range(len(files)):
        # print(str(i) )
        for j in range(0,len(files)-(i+1)):
            files[j], files[j+1] = bigyo(files[j], files[j+1])
    return files


# print(solution(['a','b','c','d','e','f']))
# print(solution(strr))
print(solution(strr2))
# print(solution(strr3))



'''
고뇌의 흔적
import re


# p = re.compile('[A-Z]*C[A-Z]*B[A-Z]*D[A-Z]*')
# match = p.match("AECB")

def bigyo(A,B):
    before, nextt = "", "" 
    # number = re.compile('[0-9]')
    alpha = re.compile('[A-Za-z]')
    number = ["0","1","2","3","4","5","6","7","8","9"]
    HA , HB = "", ""
    BA , BB = "", ""
    print()
    
    # 일단 문자열로 먼저
    for i in range(len(A)):
        if not alpha.match(A[i]) :
            HA = A[:i]
            for j in range(i,len(A)):
                if not A[j] in number:
                    BA = A[i:j]
                    break
            break

    for i in range(len(B)):
        if not alpha.match(B[i]):
            HB = B[:i]
            for j in range(i,len(B)):
                if not B[j] in number:
                    BB = B[i:j]
                    break
            break
    
    print("A의 HEAD : " + HA + "  A의 number : " + BA)
    print("B의 HEAD : " + HB + "  B의 number : " + BB)
    
    if HA.upper() == HB.upper() and BA == BB :
        return A, B
    elif HA.upper() != HB.upper() :
        if HA.upper() < HB.upper():
            return A, B
        else :
            return B, A
    elif HA.upper() == HB.upper() :
        if int(BA) > int(BB) :
            return B, A
        else :
            return A, B

    return before, nextt

# print(bigyo("foo14.txt", "fad13.txt"))

def solution(files):
    for i in range(len(files)):
        # print(str(i) )
        for j in range(0,len(files)-(i+1)):
            print(files[j])
            print(files[j+1])
            strr1, strr2 = bigyo(files[j], files[j+1])
            files[j] = strr1
            files[j+1] = strr2
            
    return files
'''