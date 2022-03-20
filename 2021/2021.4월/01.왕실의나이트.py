# 실전문제 왕실의 나이트
'''
8 * 8 좌표 평면이다.
나이트는 L형태로 이동할 수 있다. 
1. 수평으로 두칸 이동한 뒤에 수직으로 한칸 이동
2. 수직으로 두칸 이동한 뒤에 수평으로 한칸 이동
이와 같을 때, 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
행은 1~8로 표현
열은 A~H로표현한다. 
입력 예 : a1
출력 예 : 2
'''

#풀이

position = input('처음 위치를 입력하세요 : ')

move = [ (2,1), (2,-1), (-2,-1), (-2,1), (1,2), (1,-2), (-1,2), (-1,-2)]
alphabet = [ 'a', 'b','c','d','e','f','g','h']

#리스트로 변환
Plist = list(position)

for i in range(len(alphabet)) :
    #만약 알파뱃과 같다면
    if Plist[0] == alphabet[i] : 
        # 리스트 맨앞 요소 제거
        del Plist[0]
        #리스트 맨앞에 숫자를 추가
        Plist.insert(0, i+1)

count = 0
for i in move :
    if (int(Plist[0]) + i[0]) > 0 and (int(Plist[1]) + i[1] > 0) :
        count += 1

print(count)


#책의 풀이

input_data = input()
row = int(input_data[1]) #자동으로 되네
column = int(ord(input_data[0])) - int(ord('a')) + 1
result = 0
for step in move:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8 :
        result += 1

print(result)

#오늘의 파이썬
'''
ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.

'''
    
