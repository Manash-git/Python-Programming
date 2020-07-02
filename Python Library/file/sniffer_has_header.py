import csv

with open("address.csv",'r',newline='') as fl:
    sample= fl.read(40)
    header = csv.Sniffer().has_header(sample)
    print(header)
    fl.seek(0)
    detect_dialect= csv.Sniffer().sniff(fl.read(50))
    print(detect_dialect)
    print(detect_dialect.delimiter)
    print(detect_dialect.quotechar)
    print(detect_dialect.escapechar)
    
print()


with open("address.csv",'r',newline='') as fl:
    data= csv.reader(fl,detect_dialect,quotechar="'")
    
    for i in data:
        print(i)
        
print()

with open("address.csv",'r',newline='') as fl:
    data= csv.reader(fl,delimiter=',',skipinitialspace=True, quotechar="'")
    
    # for i in data:
    #     print(i)