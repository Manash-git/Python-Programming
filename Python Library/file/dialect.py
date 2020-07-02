
import csv

csv.register_dialect("myDialect",
                     delimiter='|',
                     skipinitialspace=True,
                    #  quoting=csv.QUOTE_ALL
                    #  quoting=csv.QUOTE_MINIMAL
                     quoting=csv.QUOTE_NONNUMERIC
                    #  quoting=csv.QUOTE_NONE
                     )


with open('quote_pipe.csv','r',newline='') as tf:
    info = csv.reader(tf,dialect="myDialect")
    for i in info:
        print(i)

