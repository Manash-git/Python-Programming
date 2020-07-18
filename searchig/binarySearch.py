def binarySearch(lst,key):
    lst.sort()
    print("Sorted List",lst)
    print("key=>",key)
    low=0
    high=len(lst)-1
    flag=False
    while low<=high and not flag:
        mid=(low+high)//2
        if key== lst[mid]:
            flag=True
        elif key<lst[mid]:
            high= mid-1
        else:
            low=mid+1
    
    if flag==True:
        print("Found and Index is=>",mid)
    else:
        print("Not Found")

myList=[5,1,9,4,3,8,10,6,4]
# print(set(myList))
binarySearch(list(set(myList)),4)
    
    
