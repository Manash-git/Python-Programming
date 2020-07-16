def shellsort(lst):
    gap= len(lst)//2
    print("star shorting",lst)
    while gap>0:
        for i in range(gap,len(lst)):
            curr_elmnt= lst[i]
            print("Current value",curr_elmnt)
            pos=i
            
            while pos>=gap and curr_elmnt< lst[pos-gap]:
                print("check=> ",lst[pos-gap])
                lst[pos]= lst[pos-gap]
                pos=pos-gap
            lst[pos]= curr_elmnt
            print(lst)
        gap= gap//2
        print()

mylist= [5,4,3,1,0]
shellsort(mylist)