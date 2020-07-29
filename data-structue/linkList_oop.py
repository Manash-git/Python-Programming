class Node:
    def __init__(self,value,link=None):
        self.value=value
        self.link=link
        
class LinkList:
    def __init__(self,head=None):
        self.head=head
    
    def insert(self,value):
        newNode = Node(value)
        
        # Empty Link List or not for 1st Node 
        if self.head==None:
            self.head=newNode
            return
        
        # Insert after head node
        currentNode= self.head
        while True:         # For traversing 
            if currentNode.link== None:
                currentNode.link= newNode       # if found last node then break happen
                break
            currentNode= currentNode.link       # Iterating next node
            
    def displayNode(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.value,end=" -> ")
            currentNode= currentNode.link
        print("End of Node")

link= LinkList()
link.displayNode()
link.insert(50)
link.displayNode()
link.insert(1000)
link.displayNode()
link.insert(6)
link.displayNode()
