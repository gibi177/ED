from pythonds.basic.queue import Queue
import random

def hotPotato(namelist,num):
    q=Queue()

    for name in namelist:
        q.enqueue(name)

    while q.size()>1:

        for i in range(num):
            front_person = q.dequeue()
            q.enqueue(front_person)
        
        q.dequeue() #Pessoa q esta com a batata quente é removida
    
    return q.dequeue() #retorna ultima pessoa da fila(vencedora)    


namelist = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
num_passes = random.randint(1, len(namelist))
vencedor = hotPotato(namelist, num_passes)
print(num_passes)
print("O vencedor é:", vencedor)
