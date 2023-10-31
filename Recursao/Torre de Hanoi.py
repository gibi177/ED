def hanoi(n,start,end):
    if n==1:
        movedisk(start,end)
    else:
        middle= 6-(start+end)
        hanoi(n-1,start,middle)
        movedisk(start,end)
        hanoi(n-1,middle,end)


def movedisk(start,end):
    print(start, '->', end)

hanoi(3,1,3)