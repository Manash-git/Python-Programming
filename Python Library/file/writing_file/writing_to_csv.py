import csv

# with open("data.csv",'w',newline='') as fl:
#     write= csv.writer(fl)
    
#     write.writerow(['SN',"Name","Club"])
#     write.writerow(['10',"Messi","FCB"])
#     write.writerow(['7',"Ronaldo","Juve"])
    
data_list= [[0,"Name","Club"],[10,"Messi","FCB"],[7,"Ronaldo","Juve"]]

with open("data.csv",'w',newline='') as fl:
    wr= csv.writer(fl,delimiter=":", quoting=csv.QUOTE_NONNUMERIC, quotechar="*")
    
    wr.writerows(data_list)