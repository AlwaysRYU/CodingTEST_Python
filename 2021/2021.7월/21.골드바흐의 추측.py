# 골드바흐의 추측
# https://www.acmicpc.net/problem/6588


while (True) :
    number = int(input())
    if number == 0 :
        break
    a = 1
    b = number -1 
    while ( True ) :
        if ( a % 2 == 1) & (b%2 == 1) :
            break
        a += 1
        b -= 1

    print( str(number) + " = " + str(a) + " + " + str(b))
        

