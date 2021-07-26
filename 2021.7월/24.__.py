
# 입력
number = int(input())
Array = list(map(int, input().split()))
# 젤 처음 그냥  줌
print(Array)
temp = [0] * number
temp[0] = Array[0]
print(Array)
for i in range(1,len(Array)):
    x = temp[i-1] + Array[i]
    if Array[i] >= x :
        temp[i] = Array[i]
    else :
        temp[i] = x

print(max(temp))