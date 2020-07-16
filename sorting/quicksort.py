def pivot_palace(lst,first,last):
    pivot=lst[first]
    left=first+1
    right=last
    print("pivot=> ",pivot)
    while True:
        while left<=right and lst[left]<=pivot:
            left=left+1
        while left<= right and lst[right]>=pivot:
            right=right-1
        
        if right<left:
            break
        else:
          lst[left],lst[right]= lst[right],lst[left]
    
    lst[first],lst[right]= lst[right],lst[first]
    print(lst)
    return right

def quick_sort(lst,first,last):
    
    if first<last:
        
        position= pivot_palace(lst,first,last)
        quick_sort(lst,first,position-1)
        quick_sort(lst,position+1,last)
        
        

    
    
lst=[5,10,6,9,11,12,4,3]
print("original lst=> ",lst)
l= len(lst)-1
# pivot_palace(lst,0,l)
quick_sort(lst,0,l)
print("Sorted List === ",lst)