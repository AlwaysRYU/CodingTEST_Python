S = '''   779091968 23 Sep 2009 system.zip
 284164096 14 Aug 2013 to-do-list.xml
 714080256 19 Jun 2013 blockbuster.mpeg
       329 12 Dec 2010 notes.html
 444596224 17 Jan 1950 delete-this.zip
       641 24 May 1987 setup.png
    245760 16 Jul 2005 archive.zip
 839909376 31 Jan 1990 library.dll
'''

def solution(S):
    
    strr = S.splitlines()
    answer = len(strr)
    print(strr)

    for i in strr:
        # Fsize, day, mon, year, Fname = i.split(" ")
        templist = i.split(" ")
        Fsize, day, mon, year, Fname = templist[-5], templist[-4], templist[-3], templist[-2], templist[-1]
        
        if int(year) < 1990 :
            print(Fname)
            answer -= 1
            continue
        elif int(year) == 1990 :

            if mon == "Jan" :
                answer -= 1
                continue
                

        # 파일크기
        if int(Fsize) < 245760 :
            print(Fname)
            answer -= 1
            continue
        

        
    return answer

print(solution(S))