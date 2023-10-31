from pythonds.basic.stack import Stack

def parChecker(string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(string) and balanced:
        symbol = string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top=s.pop()
                if not matches(top,symbol): #top abre "([{" e symbol fecha ")]}"
                    balanced=False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    openers= "([{"
    closers= ")]}"
    return openers.index(open) == closers.index(close) #Valor booleano que compara se o idx de open = idx de close



print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
