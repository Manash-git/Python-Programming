class Node:
    def __init__(self, value):
        self.value= value
        self.left_child = None
        self.right_child = None
        self.parent = None  # to find the parent of a tree
        


class BST:
    def __init__(self):
        self.root=None
        self.size = 0       # track the size of element of the tree
    #################    Insert  ###########################
    
    # For inserting element in a BST
    def insert(self,value):
        self.size += 1
        if self.root==None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self,value,current_node):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = Node(value)
                current_node.left_child.parent= current_node
            else:
                self._insert(value,current_node.left_child)
                
        elif value> current_node.value:
            if current_node.right_child == None:
                current_node.right_child= Node(value)
                current_node.right_child.parent=current_node
            else:
                self._insert(value, current_node.right_child)   
        else:
            print("Value already in Tree") 
    
    ##################   End of insert   ###################### 
    
    #####################  Printing Tree element #######################
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

        else:
            print("Empty Tree")
    def _print_tree(self,current_node):
        # Left -> Root -> Right
        if current_node!= None:
            self._print_tree(current_node.left_child)
            value= str(current_node.value)
            print(value,end=" - ")
            self._print_tree(current_node.right_child)
       
    # def _print_tree_inorder(self,current_node):
    #     # Left -> Root -> Right
    #     if current_node!= None:
    #         self._print_tree_inorder(current_node.left_child)
    #         print(str(current_node.value)+" - ")
    #         self._print_tree_inorder(current_node.right_child)
    
    # def _print_tree_preorder(self,current_node):
    #     # Root -> Left -> Right
    #     if current_node!= None:
    #         print(str(current_node.value)+" - ")
    #         self._print_tree_preorder(current_node.left_child)
    #         self._print_tree_preorder(current_node.right_child)
    
    # def _print_tree_postorder(self,current_node):
    #     # Left -> Right -> Root
    #     if current_node!= None:
    #         self._print_tree_postorder(current_node.left_child)
    #         self._print_tree_postorder(current_node.right_child)
    #         print(str(current_node.value)+" - ")
            
    # #############  End of Printing Tree element ###############
    
    # ############  return Size ###########################
    def no_of_elements(self):
        print("No of Tree Elements are := ",self.size)
        return
        
    ############  end of return Size ####################

    
    ############  Height ##########################
    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0
    
    def _height(self, current_node, height):
        if current_node == None:    return height
        
        left_height= self._height(current_node.left_child, height+1)
        right_height= self._height(current_node.right_child, height+1)
        
        return max(left_height, right_height)
        
        
    
    
    ############  End of Height ##################
    ############# Search ###################
    
    def search(self,value):
        if self.root!= None:
            return self._search(value, self.root)
        else:
            return False
    
    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        elif value>  cur_node.value and cur_node.right_child != None:
            return self._search( value, cur_node.right_child)
        else:
            return False
    ############ end of search ##############

####################### Call the program ###################
myBST= BST()
myBST.insert(10)
# print(myBST.print_tree())
myBST.insert(5)
# print(myBST.print_tree())

myBST.insert(15)
# print(myBST.print_tree())
myBST.insert(4)
# print(myBST.print_tree())
myBST.insert(6)
# print(myBST.print_tree())
myBST.insert(12)
# print(myBST.print_tree())
myBST.insert(20)
myBST.insert(11)
myBST.insert(3)
myBST.insert(2)
print("In-Order Print=> ",end="")
print(myBST.print_tree())
myBST.no_of_elements()
print(myBST.height())

print(myBST.search(11))


