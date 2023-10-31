#Busca Sequencial
def busca_sequencial(list, item):
    pos=0
    
    while pos<len(list):

        if list[pos]==item:
            return True       
        else:
            pos+=1
    
    return False
    

#Busca Binaria (lista ordenada)
def busca_binaria(list, item):
    pos1= 0
    pos2= len(list)-1
    found=False 

    while pos1<=pos2:
        pos3=(pos1+pos2)//2

        if list[pos3]== item:
            found=True
            return found
        
        elif item > list[pos3]:
            pos1= pos3 + 1
        elif item < list[pos3]:
            pos2= pos3 - 1 
    
    return found


#Hashing (entendi conceito, implementacao ta confusa ainda)

class hash_table:

    def __init__(self):
        self.size= 11 #tamanho da hashtable, numero primo arbitrario
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self,key,size):
     return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def put(self, key, data):

        hash_value = self.hash_function(key,len(self.slots))

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  #replace
            else:
                nextslot = self.rehash(hash_value,len(self.slots))

            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.slots))

            if self.slots[nextslot] == None:
                self.slots[nextslot]=key
                self.data[nextslot]=data
            else:
                self.data[nextslot] = data #replace
        
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
            if position == startslot:
                stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

H= hash_table()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

print(H.slots)
print(H.data)