import re

#"BACDE", "CBADF", "AECB", "BDA"]

p = re.compile('[A-Z]*C[A-Z]*B[A-Z]*D[A-Z]*')

match = p.match("AECB")
print(match)

if p.match("abc"):
    print("매치됨")


a = [1,2,3,4]
print(a.pop(1))
print(a)
