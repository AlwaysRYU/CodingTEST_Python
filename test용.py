a = []

print(len(a))
print("str + 로 합치기 ")

a, b, c = 'abc', 'def', 'ghi'

print(a+b+c)

a = ['a', 'b','c']
a.pop()

print(a)

a = (2,1) 
b = (3, 2)
print(a+b)


command = [[2,5,3],[4,4,1],[1,7,3]]
print(command[0][1])

print(14%7)

print()
strr = "우악"
strr += "새"
print(strr)


a = [2,4]
b = [1,3]
print()


a = 6
b = []

if not b :
    print("어떻게 출력")

if not b and a == 6:
    print("출력")


print("리스트비교")

a = [1,2]
b = [2,1,3,4]

if a in b :
    print("리스트 끼리 이런게 가능")
#결론 불가능하다.
print()

a = 6
b = 9
c = 12
b = bin(a)
print("2진수 변환")
print(b)
print(b[2:])
print(bin(a|c)[2:])
print()

print("반복문을 통한 리스트 생성")
print([ 0 for i in range(5)])
print()

print("리스트 다루기 ")
c = [1,2,3,4,5]
print(c[-2])
print()

