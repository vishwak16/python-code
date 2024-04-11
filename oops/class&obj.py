class Human:
    def __init__(self,n,o):
        self.name= n
        self.occupation = o

    def work(self):
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation=="cricketer":
            print(self.name ,"plays cricket")

RF =Human('roger fedrer','tennis player')
RF.work()
VK=Human('Virat Kholi','cricketer')
VK.work()