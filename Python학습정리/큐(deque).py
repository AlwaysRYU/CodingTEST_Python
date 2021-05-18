from collections import deque
#로 구현한다.

# 선언
queue = deque()

# 메소드 1:  append로 삽입
queue.append(5)
queue.append(1)
queue.append(4)
queue.append(3)
# 메소드 2: 삭제로 popleft()
queue.popleft()

print(queue)

queue.append(7)
queue.append(9)
queue.popleft()
print(queue)

# 왼쪽을 pop한다. 읽는 방식은 <--
# 메소드3 : reverse() 역순으로 전한
queue.reverse()
print(queue)
#나중에 들어온 요소부터 출력 

