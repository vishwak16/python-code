class BinTree:
    def __init__(self, val=0):
        self.data = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.data == 0:
            self.data = val
            return
        if val < self.data:
            if self.left is None:
                self.left = BinTree(val)

            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BinTree(val)
            else:
                self.right.insert(val)

    def search(self, key, icount=0):
        print(self.data)
        icount += 1
        if self.data == key:
            print(f"{key} value found")
            return icount
        if self.data < key:
            if self.left:
                return(self.left.search(key, icount))
            else:
                print(f"{key} value not found")
                return icount
        else:
            if self.right:
                return(self.right.search(key, icount))
            else:
                print(f"{key} value not found")
                return icount

    def delete(self,key):
        if self.data is None or self.data == 0:
            print("Empty Tree")
            return
        if key < self.data:
            if self.left:
                self.left = self.left.delete(key)
            else:
                print("Key Not Found")
        elif key > self.data:
            if self.right:
                self.right = self.right.delete(key)
            else:
                print("Key Not Found")
        else:
            print(f"Else: {self.data}")
            if self.left is None:
                temp = self.right
                # self = None
                return temp
            if self.right is None:
                temp = self.left
                # self = None
                return temp
            node = self.right

            while node.left:
                node = node.left

            self.data = node.data
            self.right = self.right.delete(node.data)

        return self



    def preOrder(self):
        #Root-Left-Right
        print(self.data, end=" ")
        if self.left is not None:
            self.left.preOrder()
        if self.right is not None:
            self.right.preOrder()

    def inOrder(self):
        # Left-Root-Right

        if self.left is not None:
            self.left.inOrder()
        print(self.data, end=" ")
        if self.right is not None:
            self.right.inOrder()

    def postOrder(self):
        # Left-Right-Root

        if self.left is not None:
            self.left.postOrder()
        if self.right is not None:
            self.right.postOrder()
        print(self.data, end=" ")



def PrintVals(bt):
    print("\nPreOrder")
    bt.preOrder()
    print("\nInOrder")
    bt.inOrder()
    print("\nPostOrder")
    bt.postOrder()
    print()


l = [50,30,70,20,40,60,80]
bt = BinTree()
for i in l:
    bt.insert(i)

PrintVals(bt)
# icount = 0
# print(bt.search(5, icount))

bt.delete(20)

PrintVals(bt)
