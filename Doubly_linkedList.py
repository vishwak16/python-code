class Node:
    def __init__(self):
        self.data = 0
        self.next = None
        self.prev = None

    def __str__(self):
        return "hello World"



class DLinkedList:

    def __init__(self):
        self.head = None
        self.temp = None

    def __iter__(self):

        nodes = self.head
        while nodes:
            yield nodes
            nodes = nodes.next
    def __str__(self):
        str1 = ""
        temp = self.head
        while(temp):
            str1 += str(temp.data)
            str1 += "->"
            temp = temp.next
        str1 += "None"
        return str1


    def append(self, num=0):
        nn = Node()
        if num == 0:
            num = int(input("Enter the new Node Value"))
            nn.data = num
        else:
            nn.data = num

        if self.head == None:
            # empty list
            self.head = nn
            self.temp = nn
        else:
            # list is present
            self.temp = self.head
            while(self.temp.next != None):
                self.temp = self.temp.next
            self.temp.next = nn
            nn.prev = self.temp


    def printFList(self):

        print("List is")
        self.temp = self.head
        while(self.temp != None):
            print(self.temp.data,end="->")
            self.temp = self.temp.next
        print("None")

    def printBList(self):
        print("Backward List is")
        self.temp = self.head
        while (self.temp.next != None):
            self.temp = self.temp.next
        while(self.temp != None):
            print(self.temp.data, end="->")
            self.temp = self.temp.prev
        print("None")

    def delNodeKey(self, key):
        if self.head == None:
            return False
        slow = self.head
        if slow.next == None:
            #delete the first/one node only
            if slow.data == key:
                self.head = None
                return True
        fast = slow.next
        if slow.next != None:
            if slow.data == key:
                self.head = fast
                fast.prev = None
                return True

        flag = False
        while fast:
            if fast.data == key:
                slow.next = fast.next
                fast.next = None
                flag = True
                break
            slow = slow.next
            fast = fast.next
        return flag




if __name__ == "__main__":
    dLL = DLinkedList()
    dLL.append(10)
    dLL.append(20)
    dLL.append(30)
    print("using object: ",dLL)
    dLL.printFList()
    dLL.printBList()
    dLL.delNodeKey(10)
    dLL.printFList()
    dLL.printBList()

    dllist = [node.data for node in dLL]
    print(dllist)
    print("using object: ",dLL)
