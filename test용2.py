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