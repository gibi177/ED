#Pode importar essa classe com "from pythonds.basic.stack import Stack". Aparece como erro mas funciona
class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if self.items==[]:
            return True
        return False

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())