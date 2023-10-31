from pythonds.basic.stack import Stack
stack= Stack()

def divideby2(num):

    while num > 0:
        rem = num % 2
        stack.push(rem)
        num = num // 2
    
    string = ""
    while not stack.isEmpty():
        string=string + str(stack.pop())

    return string

print(divideby2(42))
print(divideby2(3))
print(divideby2(233))
print(divideby2(8))