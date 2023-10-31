#Revisao de recursao

#Quebra o problema em subproblemas mais simples até atingir um problema tao simples que pode ser resolvido trivialmente.
#Funcao chama ela mesma, precisa de um caso base para nao chamar infinito a funcao
#A cada chamada deve-se aproximar do caso base

def fatorial(n):
    if n<=1:
        return 1
    else:
        return n* fatorial(n-1)
    

print(fatorial(8))

def fibonacci(n): #Obs primeiro elem é o zero aqui
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fatorial(8))
print(fatorial(5))

print(fibonacci(1))
print(fibonacci(5))