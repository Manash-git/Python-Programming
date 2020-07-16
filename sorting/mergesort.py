def mergesort(lst):
    print("Divide=> ",lst)
    if len(lst)>1:
        mid= len(lst)//2
        left_list=lst[:mid]
        right_list=lst[mid:]
        mergesort(left_list)
        mergesort(right_list)
        # print("done")
        i,j,k=0,0,0
    
        while i<len(left_list) and j<len(right_list):
            
            if left_list[i] < right_list[j]:
                lst[k]=left_list[i]
                k=k+1
                i=i+1
            else:
                lst[k]=right_list[j]
                k=k+1
                j=j+1
                
        while i < len(left_list):
            lst[k]=left_list[i]
            k=k+1
            i=i+1    
            
        while j<len(right_list):
            lst[k]=right_list[j]
            k=k+1
            j=j+1
        print("Merge=>",lst)

mylst=[20,1,50,40,10,5,17]
mergesort(mylst)
# print(mylst)
