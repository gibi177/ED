from pythonds.basic.deque import Deque

def palchecker(string):
    deque = Deque()

    for ch in string:
        deque.addFront(ch)

    stillEqual = True

    while deque.size() > 1 and stillEqual:
        first = deque.removeFront()
        last = deque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))