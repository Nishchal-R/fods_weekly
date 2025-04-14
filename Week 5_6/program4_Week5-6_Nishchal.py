'''Implement a program to read a CSV file and display its contents in a tabular format'''

import csv

f = ["Name","Year","GPA"]

r =[
    ["Nishchal","2006","3.43"],
]

fn = "program4.csv"

with open(fn,'w',newline= '') as csvfile:
    csv_content = csv.writer(csvfile)
    csv_content.writerow(f)
    csv_content.writerow(r)