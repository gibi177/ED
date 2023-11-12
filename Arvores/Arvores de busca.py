class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root

            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right
                else:
                    break
    
    def print(self):
        def print_rec(node, level, direction):
            if node:
                print("-" * level, node.data, direction)
                print_rec(node.left, level + 1, 'L')
                print_rec(node.right, level + 1, 'R')

        print_rec(self.root, 0, 'Root')
    
    def height(self):
         def heightRec(node):
             if node:
                hl = heightRec(node.left)
                hr = heightRec(node.right)
                return 1+max(hl,hr)
             return 0
         return heightRec(self.root)-1
    
    def leafcounter(self):
        def recursiveleafcounter(node):

            if node is not None:
                if node.left==None and node.right==None: #leaf node
                    return 1
                return recursiveleafcounter(node.left) + recursiveleafcounter(node.right)
            return 0 #root is None
        
        return recursiveleafcounter(self.root)


t= BinarySearchTree(10)
t.insert(5)
t.insert(1)
t.insert(7)
t.insert(20)
t.insert(15)
t.insert(8)
t.print()

print("height:", t.height())
print("leaves:", t.leafcounter())
