class Node:
    def __init__(self,value,link=None):
        self.value=value
        self.link=link
        
class LinkList:
    def __init__(self,head=None):
        self.head=head
        self.size=0
    
    def length(self):
        print("LinkList size => ",self.size)
    
    def insert_last(self,value):
        newNode = Node(value)
        self.size += 1
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
    
    def insert_first(self,value):
        self.size += 1
        
        newNode= Node(value)
        if self.head == None:
            self.head = newNode
            return
        else:    # Insert before head
            newNode.link = self.head
            self.head=newNode
            
    
    def remove_last(self):
        if self.size==0:
            print("empty List")
            return
        i=1
        tail= self.head
        while i < self.size-1:
            tail = tail.link
            print("Tail",tail.value)
            i+=1
        rm_value = tail.link.value
        tail.link= None
        print("Removing last value=> ",rm_value)
        self.size -=1
        
        
    def remove_first(self):
        self.size -=1
        
        rm_value= self.head.value
        self.head= self.head.link
        print("Removing first value=> ",rm_value)
        
           
             
    def displayNode(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.value,end=" -> ")
            currentNode= currentNode.link
        print("End of Node")

link= LinkList()
link.insert_last(50)
link.insert_last(40)
link.displayNode()
link.length()

link.insert_first(5)
link.displayNode()
link.length()

# link.remove_last()
# link.displayNode()
# link.length()


link.remove_first()
link.displayNode()
link.length()
