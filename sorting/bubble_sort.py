def buble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            # if lst[j]>lst[j+1]:     #ascending order
             if lst[j]<lst[j+1]:   #decending order
                lst[j],lst[j+1]=lst[j+1],lst[j]
            print(lst)
        print()

buble_sort([10,15,4,23,0])