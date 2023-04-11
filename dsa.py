
lists =[]
def push():
    if len(lists)==n:
        print("full queue")
    else:
        print("enter the element to be pushed")
        a=input()
        lists.append(a)
        print(lists)

def pop():
    if not lists:
        print("empty")
    else:
        b=lists.pop(0)
        print("the removed element is ",b)
        print(lists)

n = int(input("enter the no of elements limit....."))
while True:
    print("case ......\n 1.push \n 2.pop \n 3.exit")
    print("enter the choice : \n")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter the right one")