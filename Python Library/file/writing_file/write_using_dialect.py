import csv

csv.register_dialect("mysettings", delimiter= ",",quoting=csv.QUOTE_NONNUMERIC,quotechar="~",skipinitialspace=True)

data_list = [["SN","Country","Capital"],[1,"Bangladesh","Dhaka"],[2,"USA","New York"],[3,"Canada","Ottowa"]]

with open("test.csv",'w', newline='') as fl:
    wr= csv.writer(fl,dialect="mysettings")
    wr.writerows(data_list)