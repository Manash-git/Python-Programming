def insertionSort(lst):
    for i in range(1,len(lst)):
        
        checking_element= lst[i]
        sortList_pos= i
        
        while checking_element < lst[sortList_pos-1] and sortList_pos>0:
            lst[sortList_pos]= lst[sortList_pos-1]
            sortList_pos= sortList_pos-1
            print(lst)
            
        lst[sortList_pos] = checking_element
        print()
        
myList= [10,4,25,1,5]
insertionSort(myList)
print(myList)