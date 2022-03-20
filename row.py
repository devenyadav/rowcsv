import csv
with open('csv-sample.csv','r') as file:
    reader=csv.reader(file,delimiter=",")
    data=list(reader)
    row=len(data)
    print("the  count of row:",row) 