import csv

# with open('comma.csv','r') as f:
#     info = csv.reader(f)
#     # print(info)
#     for row in info:
        # print(row)

# with open('comma_initial_space.csv','r') as f:
#     # info = csv.reader(f,dialect='excel',skipinitialspace=True)
#     info = csv.reader(f,skipinitialspace=True)
#     # print(info)
#     for row in info:
#         print(row)

# print("\n")

# with open('comma_initial_space.csv','r') as f:
#     info = csv.reader(f,dialect='excel',skipinitialspace=True)
#     # print(info)
#     for row in info:
#         print(row)

# print("\n")

# with open('comma_initial_space.csv','r') as f:
#     info = csv.reader(f)
#     # print(info)
#     for row in info:
#         print(row)
# print('\n')

# with open("nba.txt",newline='') as tb:
#     info= csv.reader(tb,dialect='excel',delimiter='\t')
#     # info= csv.reader(tb, skipinitialspace=True)
#     for row in info:
#         print(row)

# with open("pipe.csv",'rt') as fl:
#     data= csv.reader(fl,delimiter='|')

#     for row in data:
#         print(row)

# print("\n\n")
# with open("pipe_space.csv",'rt') as fl:
#     data= csv.reader(fl,delimiter='|',skipinitialspace='true')
#     # data= csv.reader(fl,delimiter='|')

#     for row in data:
# #         print(row)

# with open("address.csv",'r',newline='') as fl:
#     # data= csv.reader(fl)
#     data= csv.reader(fl,skipinitialspace=True)
#     for row in data:
#         print(row)

# print("\n")

# with open("address.csv",'r',newline='') as fl:
#     # data= csv.reader(fl)
#     data= csv.reader(fl,skipinitialspace=True,quotechar="'")
#     for row in data:
#         print(row)

# with open("escape.csv",'r',newline='') as es:
#     info = csv.reader(es)
#     for item in info:
#      print(item)

# print('\n')

# with open("escape.csv",'r',newline='') as es:
#     info = csv.reader(es,skipinitialspace=True,escapechar='\\')
#     for item in info:
#      print(item)

print("QUOTE_ALL\n")
        
with open("quote.csv",'r',newline='') as fuck:

# As you can see, we have passed csv.QUOTE_ALL to the quoting parameter. It is a constant defined by the csv module.

# csv.QUOTE_ALL specifies the reader object that all the values in the CSV file are present inside quotation marks.
# sob quotation kichu remove kore dibe
    data= csv.reader(fuck,skipinitialspace=True)
    for item in data:
        print(item)
        
        
print('\nQUOTE_NONE\n')


with open("quote.csv",'r',newline='') as fuck:
# csv.QUOTE_NONE - Specifies the reader object that none of the entries have quotes around them.
# sob quotation je jemon ache se temon thakbe
    data= csv.reader(fuck,quoting=csv.QUOTE_NONE)
    for item in data:
        print(item)
        
print('\nQUOTE_MINIMAL\n')
        
with open("quote.csv",'r',newline='') as fuck:
# csv.QUOTE_MINIMAL - Specifies reader object that CSV file has quotes around those entries which contain special characters such as delimiter, quotechar or any of the characters in lineterminator.
    data= csv.reader(fuck,quoting=csv.QUOTE_MINIMAL)
    for item in data:
        print(item)
        
        

# print('\n')


# with open("quote.csv",'r',newline='') as fuck:

# csv.QUOTE_NONNUMERIC - Specifies the reader object that the CSV file has quotes around the non-numeric entries.
#     data= csv.reader(fuck,quoting=csv.QUOTE_NONNUMERIC)
#     for item in data:
#         print(item)

