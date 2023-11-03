n = int(input())

def repetidos(plano_estudos):
    nova_string= ''
    for elem in plano_estudos:
        if elem not in nova_string:
            nova_string+=elem
    return nova_string

for _ in range(n):
    plano_estudos = list(input())
    manha = list(input())
    tarde = list(input())
    noite = list(input())

    died = False
    for elem in manha + tarde + noite:
        if elem in plano_estudos:
            plano_estudos.remove(elem)
        else:
            print('You died!')
            died = True
            break

    if died==False:
        plano_estudos= repetidos(plano_estudos)
        if len(plano_estudos) != 0:
            resposta = ''.join(sorted(plano_estudos))
            print(f'Bora ralar: {resposta}')
        else:
            print("It's in the box!")

