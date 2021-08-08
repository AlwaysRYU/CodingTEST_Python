# 수강신청
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=3544


N = map(int, input())
subject = input().split()

Prof, Side = map(int,input().split())

total = 0
for i in subject :
    temp = int(i)
    temp = temp - Prof
    total += 1

    if(temp % Side  != 0 ) :
        total += 1
        total += (temp // Side)
    else :
        total += (temp // Side)
        
print(total)

