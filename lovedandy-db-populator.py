#!/usr/bin/env python3

#import mysql.connector
import csv

# ------------ read file
with open('vet_breed_supplement_matrix.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} dog breed {row["Dominant Breed Type"]} dog, and needs supplement {row["Top 1 Supplement"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    
    
# ------------ grab data and convert it to python data type format


# ------------ connnect to db
#mydb = mysql.connector.connect(
#  host="localhost",
#  user="yourusername",
#  passwd="yourpassword"
#)

#print(mydb)


# ------------ write data into db