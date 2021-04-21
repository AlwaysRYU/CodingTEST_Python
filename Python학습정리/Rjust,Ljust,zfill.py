# Rjust/ljust/zfill

# Rjust
# 오른쪽으로 정렬하도록 도와준다.

# str형 / 다섯칸짜리 / 빈공간은 0으로 
# 결과는 00055 우측으로 밀어준다.
temp = "55".rjust(5,'0')
print(temp)

# ljust 는 왼쪽이다.
print("55".ljust(6, '0'))

# zfill
# zfill은 0을 왼쪽에 채워준다.
val = "2".zfill(3)
print(val)
# 3칸짜리, 2칸을 채움