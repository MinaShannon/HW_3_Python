# PyBank
#if __name__=="__main__"
import csv
import os
csvpath=os.path.join("..""PyBank.csv")
with open(csvpath,newline="") as csvfile:
    csv.reader(csvfile,delimiter=",")
    csvheader=next(csvfile)
    months=enumerate(row[0])-1
    print(months)
    for rows in csvreader: