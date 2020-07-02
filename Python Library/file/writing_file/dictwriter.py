
import csv

with open("demo.csv",'w', newline='') as fl:
    
    head=["Player Name","Club"]
    wr= csv.DictWriter(fl,fieldnames=head)
    wr.writeheader()
    
    wr.writerow({"Player Name":"Messi","Club":"FCB"})
    
    wr.writerow({"Player Name":"Neymar","Club":"PSG"})