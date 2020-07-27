# Basic way
class LinkedList:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode= nextNode

# creating object

node1= LinkedList(5)
node2= LinkedList(10)
node3= LinkedList(22)
node4= LinkedList(3)

# now linking between nodes

node1.nextNode= node2
node2.nextNode=node3
node3.nextNode= node4

# printing the value

currentNode=node1
while True:
    
    print(currentNode.value,end="-> ")
    if currentNode.nextNode==None:
        print("None")
        break
    currentNode= currentNode.nextNode