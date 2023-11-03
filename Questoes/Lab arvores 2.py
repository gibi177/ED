def altura(raiz):
    if raiz is None:
        return 0

    if len(raiz) > 0:
        if raiz[1]==[] and raiz[2]==[]:
            return 0
        altura_esq = altura(raiz[1])
        altura_dir = altura(raiz[2])
    
    elif raiz==[]:
        return 0

    return 1+ max(altura_esq, altura_dir)

raiz=[1, [2, [3, [4, [], []], [5, [], []]], [6, [7, [], []], [8, [], []]]], [9, [10, [], []], [11, [], []]]]
print(altura(raiz))



