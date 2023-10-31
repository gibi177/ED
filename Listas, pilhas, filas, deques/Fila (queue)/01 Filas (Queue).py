# importando a fila: from pythonds.basic.queue import Queue
class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue (self,item): #add
        self.items.append(item)
    
    def dequeue (self): #remove
        self.items.pop(0)

    def size(self):
        return len(self.items)

q= Queue()    
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
