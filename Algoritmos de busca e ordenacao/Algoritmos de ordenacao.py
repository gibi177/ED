#Bubble sort (Compara o 1o elem com o 2o dps com o 3o... no final da primeira passagem o maior elemento vai estar no ultimo index)

def bubble_sort (alist): #0.28ms
    compare=len(alist)-1
    
    while compare>0:
        for i in range(compare):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
        
        compare-=1

    return alist
                
                
def short_bubble_sort(alist):
    exchanges=True
    compare=len(alist)-1
    
    while compare>0 and exchanges:
        exchanges= False
        for i in range(compare):
            if alist[i]>alist[i+1]:
                exchanges=True
                alist[i],alist[i+1] = alist[i+1],alist[i]
            
        compare-=1
    
    return alist

#Selection sort (busca menor elemento pelo indice, troca elemento no lugar do 1o indice)

def selection_sort(alist): #0.29
    
    for i in range(len(alist)):
        min_index=i
        
        for j in range(i+1,len(alist)):
            if alist[min_index]>alist[j]:
                min_index=j
                
        alist[i], alist[min_index] = alist[min_index], alist[i]   

    return alist      


#Quick sort (Pivo indice 0, add elem < pivo lista esquerda e > pivo lista direita. Chama recursivamente em cada lista)

def quick_sort(alist): #0.46ms

    if len(alist) <=1:
        return alist
    
    left, pivot, right = reorder(alist)
    left = quick_sort(left)
    right = quick_sort(right)
    left.append(pivot)
    left.extend(right)
    return left

def reorder(alist):  
    left=[]
    right=[]
    pivot= alist[0]  

    for elem in alist[1:]:
        if elem<pivot:
            left.append(elem)
        elif elem>=pivot:
            right.append(elem)

    return left, pivot, right


#Insertion sort (separa lista em 2 mentalmente, esq 1 elemento. Vai comparando com os indices anteriores pra saber pos)

def insertion_sort(alist): #0.29ms

    for i in range(1, len(alist)):

        while alist[i-1] > alist[i] and i>0:
            alist[i], alist[i-1] = alist[i-1], alist[i]
            i-=1

    return alist


#Shell sort (Quebra lista em intervalos e aplica shell sort? OBS:precisa saber tamanho n da lista)

def shell_sort(alist, n): #0.55ms

    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = alist[i]
            j = i
            while j >= interval and alist[j - interval] > temp:
                alist[j] = alist[j - interval]
                j -= interval

            alist[j] = temp
        interval //= 2
    
    return alist


#Merge sort (vai quebrando lista pela metade ate ficar varias de tam 1, dps vai juntando uma com a outra no sentido inverso ja na ordem certa)

def merge_sort(alist):

    if len(alist)>1:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]

        #Chama recursivo dividindo em listas menores
        merge_sort(left)
        merge_sort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k]=left[i]
                i=i+1
            else:
                alist[k]=right[j]
                j+=1
            k+=1

        while i < len(left):
            alist[k]=left[i]
            i+=1
            k+=1

        while j < len(right):
            alist[k]=right[j]
            j+=1
            k+=1
    
    return alist