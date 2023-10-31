class Person:
    def __init__(self, name, age, height, weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.actions=[]

    def add_action(self, action_added):
        self.actions.append(action_added)
   
user= Person('Felipe', 19, 180, 81)
user.add_action('Walk')
user.add_action('Jump')

print(user.weight)
print(user.actions)

