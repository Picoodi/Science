#This is a little Programm to create a binary tree

#the Node Class with Functions to create and update the Node
class Node():
    def __init__(self, value:float, name: str) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.name = name
      
    def valueup(self,x):
        self.value += x
    
    def valuedown(self,x):
        self.value -= x

    def createleftchild(self,x, name):
        self.left = Node(x, name)

    def createrightchild(self,x, name):
        self.right = Node(x, name)



# a recursive function that prints the trees data 
def print_Tree(Node, depth = 0):
    print(depth,"  ",Node.value,"  ",Node.name)
    if Node.left:
        print_Tree(Node.left, depth+1)
    if Node.right:
        print_Tree(Node.right, depth+1)




#Test code to create some data and see if it works
root = Node(0, "Root")
root.createleftchild(1,"left")
root.left.createleftchild(2, "childleft")
root.createrightchild(10, "right")
root.right.createrightchild(11, "childright")
root.right.right.createleftchild(29,"childrightrightleft")
root.left.createrightchild(31, "childleftright")
print_Tree(root)
