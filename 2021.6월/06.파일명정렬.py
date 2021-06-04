# 파일명 정렬
# https://programmers.co.kr/learn/courses/30/lessons/17686?language=python3

strr = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
strr2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
strr3 = ["abc", "Abc", "ABC","aVC" ]

def bigyo(A,B):
    before, nextt = "", "" 
    number = ["0","1","2","3","4","5","6","7","8","9"]
    print()
    # 일단 문자열로 먼저
    for i in range(len(A)):
        if A[i] in number :
            HA = A[:i]
            for j in range(i,len(A)):
                if not A[j] in number:
                    BA = A[i:j]
                    break
            break
    for i in range(len(B)):
        if B[i] in number :
            HB = B[:i]
            for j in range(i,len(B)):
                if not B[j] in number:
                    BB = B[i:j]
                    break
            break
    
    print("A의 HEAD : " + HA + "A의 number : " + BA)
    print(HB, BB)
    
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
    answer = []
    for i in range(len(files)):
        for j in range(0,len(files)-(i+1)):
            strr1, strr2 = bigyo(files[j], files[j+1])
            files[j] = strr1
            files[j+1] = strr2
            print(j,end= " ")
    return files


# print(solution(strr))
print(solution(strr2))
# print(solution(strr3))