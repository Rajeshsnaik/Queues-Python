import queue
stack = queue.Queue(3)
stack.put(20)
stack.put(26)
stack.put(44)
stack.put(33,timeout=1)  #put(item, block=True, timeout)
stack.get()

# --------forward data entering--------
queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
queue.pop(0)
queue.pop(0)
print(queue)

#--------backward entering data ---------
queue=[]
queue.insert(0,10)
queue.insert(0,20)
queue.pop()
print(queue)

queue=[]
def enqueue():
    element= input("enter the element")
    queue.append(element)
    print(element,"is added")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("removed element", e)
def display():
    print(queue)

while True:
    print("select one 1.add 2.remove 3.show 4.quit")
    choice = int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter correct choice")



import collections
q=collections.deque()
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.popleft()
print(q)



import queue
q = queue.PriorityQueue()
q.put(10)
q.put(20)
q.get()
print(q)         


#priority queue using tuple
q = []
q.append((1,'a'))
q.append((2,'b'))
q.append((3,'c'))
q.append((4,'d'))
q.sort(reverse=True)
q.pop(0)
print(q)
