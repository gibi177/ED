#Ta meio mais ou menos 
class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def insert_left(self, data):
        if self.left is None:
            self.left = BinaryTree(data)
        else:
            new = BinaryTree(data)
            new.left = self.left
            self.left = new

    def insert_right(self, data):
        if self.right is None:
            self.right = BinaryTree(data)
        else:
            new = BinaryTree(data)
            new.right = self.right
            self.right = new

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_root(self):
        return self.root

    def set_root_val(self, value):
        self.root = value


r = BinaryTree(0)
print(r.get_root())
print(r.get_left_child())
print(r.get_right_child())

r.insert_left(1)
print(r.get_left_child().get_root())  
r.insert_right(2)
print(r.get_right_child().get_root())  
r.insert_left(3)
