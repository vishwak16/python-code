class Node:
    def __init__(self, val=None):
        self.data = val
        self.next = None

class LList:

    def __init__(self):
        self.head = None
        self.temp = None
        self.__LenList = 0

    def __iter__(self):

        nodes = self.head
        while nodes:
            yield nodes
            nodes = nodes.next

    def __str__(self):
        nodes = self.head
        str1 = ""
        while(nodes != None):
            str1 += str(nodes.data)
            str1 +="->"
            #print(str1)
            nodes = nodes.next
        str1 += "None"
        return str1

    def addNodeBeg(self, val):
        nn = Node(val)
        if self.head == None:
            #empty list
            self.head = nn
        else:
            nn.next = self.head
            self.head = nn
        self.__LenList += 1

    def append(self, val):
        nn = Node(val)
        if self.head == None:
            #empty list
            self.head = nn
            self.temp = nn
        else:
            #list is present
            self.temp = self.head
            while(self.temp.next != None):
                self.temp = self.temp.next
            self.temp.next = nn

        self.__LenList += 1

    def getLen(self):
        return (self.__LenList)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def delNode(self, key):
        slow = self.head
        fast = slow.next
        if slow is None:
            print("List is empty")
            return False
        if slow.next == None and slow.data == key:
            # if only one node
            self.head = None
            self.__LenList -= 1
            return True
        if slow.data == key:
            # del beg Node
            self.head = slow.next
            self.__LenList -= 1
            return True
        while fast:
            if fast.data == key:
                # print(f"slow: {slow.data}, fast: {fast.data}")
                slow.next = fast.next
                self.__LenList -= 1
                return True
            slow = slow.next
            fast = fast.next
        return False

    def delNodePos(self, pos):
        slow = self.head
        fast = slow.next
        count = 0
        if slow is None:
            print("List is empty")
            return False
        if pos > self.__LenList:
            return False
        if slow.next == None and count == pos:
            # if only one node
            self.head = None
            self.__LenList -= 1
            return True
        if count == pos:
            # del beg Node
            self.head = slow.next
            self.__LenList -= 1
            return True
        while fast:
            count+=1
            if count == pos:
                # print(f"slow: {slow.data}, fast: {fast.data}")
                slow.next = fast.next
                self.__LenList -= 1
                return True
            slow = slow.next
            fast = fast.next
            # count += 1
        return False

    def pop(self):
        slow = self.head

        if slow is None:
            # print("List is empty")
            return False
        if slow.next == None:
            # if only one node
            ret = self.head.data
            self.head = None
            self.__LenList -= 1
            return ret
        fast = slow.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        # print(f"slow: {slow.data}, fast: {fast.data}")
        ret = fast.data
        slow.next = None
        self.__LenList -= 1
        return ret


def printListOut(head):
    while(head):
        print(head.data,end="->")
        head = head.next



if __name__ == "__main__":
    ll = LList()
    print([node.data for node in ll])
    '''
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    print(ll)
    ll.addNodeBeg(201)
    print(ll)
    print([node.data for node in ll])
    print(ll.getLen())
    ll.addNodeBeg(201)
    print(ll)
    #ll.printList()
    print(ll)
    if ll.delNode(110) == False:
        print("Key Not Found")
    else:
        print(ll)
        print(ll.getLen())

    rStatus = ll.pop()
    if rStatus == False:
        print("List is empty")
    else:
        print(f"{rStatus} is popped out")
        print(ll)
        print(ll.getLen())

    rStatus = ll.pop()
    if rStatus == False:
        print("List is empty")
    else:
        print(f"{rStatus} is popped out")
        print(ll)
        print(ll.getLen())

    rStatus = ll.pop()
    if rStatus == False:
        print("List is empty")
    else:
        print(f"{rStatus} is popped out")
        print(ll)
        print(ll.getLen())

    rStatus = ll.pop()
    if rStatus == False:
        print("List is empty")
    else:
        print(f"{rStatus} is popped out")
        print(ll)
        print(ll.getLen())

    rStatus = ll.pop()
    if rStatus == False:
        print("List is empty")
    else:
        print(f"{rStatus} is popped out")
        print(ll)
        print(ll.getLen())

    rStatus = ll.pop()
    if rStatus == False:
        print("List is empty")
    else:
        print(f"{rStatus} is popped out")
        print(ll)
        print(ll.getLen())
    ll.addNodeBeg(101)
    ll.printList()
    '''
    ll.append(10)
    ll.append(22)
    ll.append(30)
    ll.append(20)
    ll.append(110)
    print(ll)
    head = ll.getHead()
    print("print list outside the class")
    printListOut(head)
    ll.delNodePos(1)
    print()
    print(ll)
