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



# ----<우선순위 큐 >----
'''
데이터 추가는 맘대로 해도 된다.
출력은 가장 작은 값부터 제거한다.
'''
from queue import PriorityQueue
#선언

#생성
que = PriorityQueue()

#디폴트 사이즈  설정
que = PriorityQueue(maxsize=8)
#이럴 경우 8로 설정됨

# 원소 추가
que.put(4)
que.put(7)
que.put(1)
que.put(3)
# que.put(우선순위, 값)의 튜플 형태로 데이터를 추가하고 제거할 수 있다.
que.put(8,'IU')
print(que)
#이렇겐 못봄

# 삭제
que.get()

print(que.get())
