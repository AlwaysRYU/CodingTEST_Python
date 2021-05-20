cloud = "undertalestory"

print(cloud[:2:])
print(cloud[2:4:])
print(cloud[4:6:])


nine = "abc"
jamiro = cloud+nine
print(jamiro)
print()

print(6/2)

a = [1,2,3,4,5,6,7,8,9]

for i in range(4,9,4):
    print(i)


print()
strings = ["sun", "bed"]
print(strings[0][2])


b = [[1,2],[3,4],[5,6]]
del b[0]
print(b)
c = [1,2,3,4]

for i in range(len(c)-1,0 , -1):
    print(c[i])

d = [1,2,3,4,5]

d[2] = d[3]
print(d)

e = [1] * 10
print(e)

f = d.pop(0)
print(d)
print(f)

g = "when you gonna learn"
for i in range(len(g)):
    print(g[i])

h = "이럴거면그러지말지"
print(h[:2])
print(h[2:])

j = "(((()))))"
jj = j.replace('(','-')
jjj = jj.replace(')','(')
jjjj = jjj.replace('-',')')
print(jjjj)


k = "123"
l = int(k)
print(k)

for i in range(9,1,-1):
    print(i)

m = ['94','9','5','52','534', '53' ]
m.sort(reverse=True)
# m.sort()
print(m)

print((lambda x : x*3)('2'))

print(type(3) == int)

print(m)
print(m[-1])


a = ["123","12","1234"]
b = sorted(a, key=len)
print(b)

c = 5

from itertools import combinations

for i in range(1,c):
    print(list(combinations(range(c),i)))


listt = [[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]
print("중복")
print(listt[0][0][1])
print()
print()

print()
print("뒤에 없을 때 정렬테스트")
a = [30,31,32,34,38,36,35,37,376,378,387,361,366,365,361,360]
b = [str(i) for i in a]
print(b)
# c = sorted(b,key = lambda x : x[1] f len(x) == 1  , reverse=True)
c = sorted(b,reverse=True)
print(c)
dd = ["313131","333","387387387","383838"]
dd.sort(reverse=True)
print(dd)
