#from pythonds.basic.deque import Deque
class Deque():
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]
    
    def display(self):
        return print(self.items)

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)
    
    def removeFront(self):
        self.items.pop()
    
    def removeRear(self):
        self.items.pop(0)
    
    def size(self):
        return len(self.items)
    

d=Deque()
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
d.removeRear()
d.removeFront()
d.display()