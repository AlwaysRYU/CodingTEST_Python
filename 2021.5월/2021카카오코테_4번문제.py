def solution2(n, start, end, roads, traps):
    answer = 0


    return answer

# print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]], [2]))
# print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3]))


class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class SList(object):
    def __init__(self):
        self.head = Node(None)
        self.size = 0
        
    def listSize(self):
        return self.size
    
    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True
        
    def selectNode(self, idx):
        if idx >= self.size:
            print("Index Error")
            return None
        if idx == 0:
            return self.head
        else:
            target = self.head
            for cnt in range(idx):
                target = target.next
            return target
        
    def appendleft(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.size += 1
    
    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        else:
            target = self.head
            while target.next != None:
                target = target.next
            newtail = Node(value)
            target.next = newtail
            self.size += 1
        
    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        elif idx == 0:
            self.head = Node(value, self.head)
            self.size += 1
        else:
            target = self.selectNode(idx-1)
            if target == None:
                return
            newNode = Node(value)
            tmp = target.next
            target.next = newNode
            newNode.next = tmp
            self.size += 1
        
    def delete(self, idx):
        if self.is_empty():
            print('Underflow: Empty Linked List Error')
            return
        elif idx >= self.size:
            print('Overflow: Index Error')
            return
        elif idx == 0:
            target = self.head
            self.head = target.next
            del(target)
            self.size -= 1
        else:
            target = self.selectNode(idx-1)
            deltarget = target.next
            target.next = target.next.next
            del(deltarget)
            self.size -= 1
            
    def printlist(self):
        target = self.head
        while target:
            if target.next != None:
                print(target.data, '-> ', end='')
                target = target.next
            else:
                print(target.data)
                target = target.next

    def gap(self):
        return self.head

    


ex1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	
ex2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

def solution(n, k, cmd):
    answer = ''
    before = [ str(i) + "번째 캐릭터" for i in range(n)]
    now = k

    mylist = SList()
    for i in range(n):
        mylist.append(i)
    mylist.printlist()

    templist = []
    
    for i in range(len(cmd)):
        if cmd[i][0] == "U":
            print("위로")
            iss = cmd[i].split(" ")
            now = now - int(iss[1])
        
        elif cmd[i][0] == "D":
            iss = cmd[i].split(" ")
            now = now + int(iss[1])

        elif cmd[i][0] == "C":
            templist.append(mylist.gap)
            print(templist)
            mylist.delete(now)
        
        elif cmd[i][0] == "Z":
            print("복구")
            # belist.insert(tempnumber[-1],tempnumber[-1])
            # del tempnumber[-1]
            # if tempnumber[-1] <= now :
            #     now += 1
            #     if now >= len(belist) : now = len(belist)-1
            # print("현재 위치 : " + str(belist[now]))

    # print("연산후 테이블 : " + str(belist))

    # realbefore = [ i for i in range(n)]

    # while realbefore :
    #     if realbefore[0] == belist[0]:
    #         answer += "O"
    #         del realbefore[0]
    #         del belist[0]
    #     else :
    #         answer += "X"
    #         del realbefore[0]


    return answer

    
print(solution(8,2,ex1))
print(solution(8,2,ex2))



