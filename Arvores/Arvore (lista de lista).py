#Arvores usando lista de listas

#"a" é raiz, aponta pra "b" e "c". "b" aponta pra "d" e "e", que nao apontam pra nada. "c" aponta so pra "f", que n aponta pra nada
mytree= ['a',   #root
      ['b',  #left subtree
       ['d', [], []],
       ['e', [], []] ],
      ['c',  #right subtree
       ['f', [], []],
       [] ]
    ]


print(mytree)
print('left subtree = ', mytree[1])
print('root = ', mytree[0])
print('right subtree = ', mytree[2])

#Criando e manipulando arvores
def BinaryTree(root):
    return [root,[],[]]

def InsertLeft(tree,item): 
    aux= tree.pop(1) #elem 0 da arvore é a raiz, 1 a sub da esq e 2 a sub da dir
    if len(aux)>0:
        tree.insert(1,[item,aux,[]]) #Como aux ja é uma subarvore, n precisa botar entre []
    else:
        tree.insert(1,[item,[],[]])

def InsertRight(tree,item):
    aux= tree.pop(2) 
    if len(aux)>0:
        tree.insert(2,[item,[],aux]) #item é subroot, esq [] e dir subarvore aux
    else:
        tree.insert(2,[item,[],[]])

def getRootVal(tree):
    return tree[0]

def setRootVal(tree,newVal):
    tree[0] = newVal

def getLeftChild(tree):
    return tree[1]

def getRightChild(tree):
    return tree[2]

def preorder(tree):
    if tree != []:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
  if tree != []:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

def postorder(tree): #Subesq dps subdir dps raiz
    if tree != []:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

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


r = BinaryTree(1)

InsertLeft(r,3)
InsertLeft(r,2)
InsertRight(r,5)
InsertRight(r,4)

print(getLeftChild(r))
print(getRightChild(r))

InsertRight(getLeftChild(r),6) #add 6 a direita do 2 
print(getLeftChild(r))

node_add= getLeftChild(getLeftChild(r)) #elem a esquerda da esquerda da raiz(3)
InsertRight(node_add,7)

print(r)
print(altura(r))
print(getLeftChild(r))
print(getRightChild(r))