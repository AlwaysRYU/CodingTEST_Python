# Chapter5 DFS/BFS
# 2021.04.10.
# 스택
'''
탐색? : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
대표적 탐색알고리즘
DFS
BFS
오버플로 : 특정한 자료구조가 수용할 수 있는 데이터가 가득 찬 상태에서 삽입 연산을 수행
언더플로 : 데이터가 전혀없는 상태에서  삭제
'''
'''
스택 = 박스쌓기
선입후출/후입선출 구조

'''

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
stack.append(13)
stack.append(42)
stack.append(22)
stack.append(234)
stack.append(55)
stack.append(93)


print(stack)
print(stack[::-1])
#역순으로 출력

print(stack)
print(stack[::2])
# 0 2 4 6 8 ... 이렇게 출력

print(stack[::-2])
# 맨뒤부터 2 출력