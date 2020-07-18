def linearSearch(lst,key):
    result_list=[]
    flag=False
    
    for i in range(len(lst)):
        if lst[i]==key:
            flag=True
            result_list.append(i)   # take index no
    
    if flag==True:
        print(result_list)
        for i in range(len(result_list)):
            print("Index No=> ",result_list[i])
    else:
        print("not found")

key=1
myList=[1,5,9,4,3,2,4,5,1,3,1,0,10]
linearSearch(myList,key)