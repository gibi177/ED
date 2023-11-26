class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        def insert_recursive(data,current):
            new_node= Node(data)

            if current==None: #raiz é None
                self.root=new_node

            elif data<current.data:
                if current.left==None:
                    current.left=new_node
                else:
                    insert_recursive(data,current.left)
            
            elif data>current.data:
                if current.right==None:
                    current.right=new_node
                else:
                    insert_recursive(data,current.right)
              
        insert_recursive(data,self.root)
    
    def display(self): #preorder
        def display_rec(node, level, direction):
            if node:
                print("-" * level, node.data, direction)
                display_rec(node.left, level + 1, 'L')
                display_rec(node.right, level + 1, 'R')

        display_rec(self.root, 0, 'Root')
    
    def height(self,node):
        def heightRec(cur_node):
            if cur_node:
                hl = heightRec(cur_node.left)
                hr = heightRec(cur_node.right)
                return 1 + max(hl,hr)
            return 0
        return heightRec(node)-1
    
    def leafcounter(self):
        def recursiveleafcounter(node):

            if node:
                if node.left==None and node.right==None: #leaf node
                    return 1
                return recursiveleafcounter(node.left) + recursiveleafcounter(node.right)
                
            return 0 #root is None   
        return recursiveleafcounter(self.root)
    
    def delete(self,data):
        def delete_recursive(node,data):
            if node is None: #raiz é none
                return None
            
            #Percorre a arvore
            if data<node.data:
                node.left = delete_recursive(node.left,data)
            elif data>node.data:
                node.right = delete_recursive(node.right,data)
            
            #Vc ta retornando pro valor que quer remover
            #Ex:10r,nonee,20d. 20,15e,noned. Quer remover 20. enquanto ta no 10, fala q o 20 é igual delrecurs 20.Cai no caso que esq existe,dir none, retorna esq no lugar do 20,assim remove o 20
            else:
                if not node.left and not node.right: #nao tem filhos, dir e esq sao none
                    return None
                elif not node.left and node.right: #esq none, dir existe
                    return node.right
                elif not node.right and node.left: #dir none, esq existe
                    return node.left
                
                else: #tem 2 filhos
                    cur=node.right
                    while cur.left is not None: #Minimo subarvore direita
                        cur=cur.left
                    
                    node.data=cur.data #copia minimo subarvore dir pra o node a ser removido
                    node.right=delete_recursive(node.right,cur.data) #deleta recursivamente o min subarvore dir

            return node     
        self.root= delete_recursive(self.root,data)
    
    def search(self,data):
        def search_recursive(node,data):
            if node is None:
                return False
            
            elif data==node.data: #Caso base, achou
                return True
            
            elif data<node.data:
                return search_recursive(node.left,data)
            
            elif data>node.data:
                return search_recursive(node.right,data)  

        return search_recursive(self.root,data)
    
    def isSymmetric(self):
        def checksymmetry(node1,node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            
            return node1.data==node2.data and checksymmetry(node1.left,node2.right) and checksymmetry(node1.right,node2.left)

        return checksymmetry(self.root.left, self.root.right)
    
    def isBalanced(self):
        leftheight = self.height(self.root.left) 
        rightheight = self.height(self.root.right)
        
        if abs(leftheight - rightheight) <=1:
            return True
        return False
    
    def invert(self):
        def invert_recursive(node):
            if node:
                node.left, node.right = node.right, node.left
            
                invert_recursive(node.left)
                invert_recursive(node.right)

        invert_recursive(self.root)
    
    def findMin(self):
        def findMinrecursive(node):
            if node:
                if node.left is None and node.right is None:
                    return node.data
                elif node.left is None and node.right:
                    return node.data
                return findMinrecursive(node.left)
        
        return findMinrecursive(self.root)
    
    def findMax(self):
        def findMaxrecursive(node):
            if node:
                if node.left is None and node.right is None:
                    return node.data
                elif node.right is None and node.left:
                    return node.data
                return findMaxrecursive(node.right)
        
        return findMaxrecursive(self.root)


t= BinarySearchTree(10)
t.insert(5)
t.insert(1)
t.insert(7)
t.insert(20)
t.insert(15)
t.insert(8)

t.display()
print() #pula linha

t.delete(5)
t.display()
print() #pula linha

print("Search?", t.search(15))
print("Search?", t.search(16))
print()

print("height:", t.height(t.root))
print("leaves:", t.leafcounter())
print()

print("Is symmetric?", t.isSymmetric())
print()

print("Is balanced?", t.isBalanced())
print("Left height:", t.height(t.root.left))
print("Right height:", t.height(t.root.right))
print()

print("Min value:", t.findMin())
print("Max value:", t.findMax())
print()

t.invert() #invertido ent mt coisa n vai mais funcionar direito
t.display()