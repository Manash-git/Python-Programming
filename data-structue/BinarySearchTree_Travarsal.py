class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

# Manual Tree
class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)
    
    def printTree(self, travarsal_type):
        
        if travarsal_type == "pre-order":
            return self.preorder(tree.root,"")
        elif travarsal_type == "in-order":
            return self.inorder(tree.root)
        elif travarsal_type == "post-order":
            return self.postorder(tree.root)
        else:
            return print("Invalid Input")
    
    def preorder(self,start,travarsal):
        # Root -> Left -> Right
        if start:
            travarsal= travarsal + (str(start.value)+ " - ")
            # print("Test=>",travarsal)
            travarsal = self.preorder(start.left,travarsal)
            travarsal = self.preorder(start.right,travarsal)
        # print("Out of If")
        return travarsal
    
    
    def inorder(self,start):
        # Left -> Root -> Right
        if start:
            self.inorder(start.left)
            print(start.value,end=" - ")
            self.inorder(start.right)
            
        
    def postorder(self, start):
        # Left -> Right -> Root
       if start:
            self.inorder(start.left)
            self.inorder(start.right)
            print(start.value,end=" - ")
            
tree= BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)

tree.root.left.left= Node(4)
tree.root.left.right= Node(5)

tree.root.right.left= Node(6)
tree.root.right.right= Node(7)
print(tree.printTree("pre-order"))
print(tree.printTree("in-order"))
print(tree.printTree("post-order"))


        