import re

#"BACDE", "CBADF", "AECB", "BDA"]

p = re.compile('[A-Z]*C[A-Z]*B[A-Z]*D[A-Z]*')

match = p.match("AECB")
print(match)

if p.match("abc"):
    print("매치됨")

p2 = re.compile('[A-Za-z]')

if not p2.match("a"):
    print("매치매치")


a = [1,2,3,4]
print(a.pop(1))
print(a)


print()
print()
print()
print()
if "AA" < "AB" :
    print("크다")
else :
    print("작다")

print("-".upper())

print()
print()
print()


print(4%3)

print(sum([1,2,3]))
print(min(1,2,3))
print("abcd"[1])
array = sorted([2,3,4,1])
print(array)
if "a" < "b" :
    print(1234)

a = ["1", "2", "3", "4" ]

for i in (2,a):
    print(i)