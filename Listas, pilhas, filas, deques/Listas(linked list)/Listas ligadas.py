class Node:  #Nos sao componentes de listas que se encadeiam entre si, sao compostos pelo dado e pelo seu "indicador de próximo"
    def __init__(self, data=None): #data=None é o valor default de fata. Se nenhum valor for passado, o default sera usado
        self.data= data
        self.next=None

class LinkedList: #Nao ordenada
    def __init__(self):
        self.head = None #Tava fazendo self.head = Node(). Errado pq head n tem atributo next que tem no Node.
    
    def append(self, data): 
        new_node = Node(data)
        if self.head == None: #Se head aponta pra none
            self.head = new_node #head vai apontar pro novo node (adiciona 1o elem)
            return #para o funcionamento do metodo (ja add)
        
        cur = self.head
        while cur.next != None:
            cur = cur.next
        
        cur.next = new_node #cur.next que apontava pra none vai apontar pra new_node 

    def add(self,item): #Add no começo da lista
        temp = Node(item) #cria novo node que vai add
        temp.next = self.head #temp aponta para onde head esta apontando (1o elemento da lista)
        self.head = temp #head aponta para temp. Fica head -> temp -> 1o elemento que virou segundo

    def __len__(self): # o double underline faz com que funcione: len(lista) em vez de lista.len()
        cur = self.head #cur "aponta" pra onde head esta referenciando, cur esta "embaixo" do 1o elemento e seu next aponta pro 2o elem
        total_nodes = 0 #Contador do total de nodes

        while cur != None: #percorre lista
            total_nodes+=1
            cur=cur.next
        
        return total_nodes
    
   
    def display(self): 
        elems = []
        cur = self.head  

        if cur==None:
            return print(elems)
        else:
            while cur != None:
                elems.append(cur.data)
                cur = cur.next

        print(elems)


    def search(self,item):
        cur = self.head

        while cur != None:
            if cur.data == item:
                return True
            else:
                cur = cur.next
        
        return False   
    
    def remove(self, item):
        cur = self.head
        prev = None

        while cur != None:
            if cur.data == item:
                if prev == None:
                    self.head = cur.next #head aponta pro elem dps de cur(pula o cur)
                else:
                    prev.next = cur.next #prev aponta para o no dps de cur, pulando o cur (elemento a remover). O next é pra onde ele aponta entao prev.next é pra onde prev aponta    
                return
            else:
                prev = cur
                cur = cur.next
        
        print('Item not found')   

    def __getitem__(self,index): #__getitem__ permite acessar a funcao passando o paramentro index por []. ex. lista[0]

        if index < 0 or index >= len(self):
            print('Index out of range')
            return None
        
        cur_idx = 0
        cur= self.head
        while cur_idx < index: #Percorre ate achar o indice certo
            cur_idx += 1
            cur = cur.next

        return cur.data
    
    def erase(self, index): #remove pelo indice
        if index < 0 or index >= len(self):
            print('Index out of range')
            return None
        
        prev = None
        cur_idx = 0
        cur= self.head
        while cur_idx < index: 
            prev = cur
            cur = cur.next
            cur_idx += 1

        if prev == None: #Removendo indice 0
            self.head = cur.next
        else:
            prev.next = cur.next

        

my_list= LinkedList()
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()

print(my_list.search(2))

my_list.remove(2)
my_list.display()
print(my_list.search(2))

print(len(my_list))

print(my_list[0])

my_list.erase(0)
my_list.display()

