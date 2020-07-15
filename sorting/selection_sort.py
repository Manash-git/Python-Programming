def selection_ascending(lst):
    print("Original List: ",lst)
    
    for i in range(len(lst)):
        min_val= min(lst[i:])
        min_val_index= lst.index(min_val)
        # swap
        lst[i],lst[min_val_index]=lst[min_val_index],lst[i]
    print("Sorted in ascending order: ",lst)
    
def selection_decending(lst):
    print("Original List: ",lst)
    
    for i in range(len(lst)):
        max_val= max(lst[i:])
        max_val_index= lst.index(max_val)
        # swap
        lst[i],lst[max_val_index]=lst[max_val_index],lst[i]
    print("Sorted in decending order: ",lst)
    

data=[50,100,2,0,9,4,6,8,15,10]
# selection_ascending(data)
# selection_decending(data)
print()
def efficient_selection_sort(lst):
    print("Original List: ",lst)
    
    for i in range(len(lst)):
        min_val= min(lst[i:])
        min_val_index= lst.index(min_val,i) # here i is remove duplication
        # swap
        
        lst[i],lst[min_val_index]=lst[min_val_index],lst[i]
        print("Sorted in ascending order: ",lst)
    
        
data=[50,100,2,0,9,4,6,8,15,0,10]
efficient_selection_sort(data)
