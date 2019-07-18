#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# In[1]:

# -------------------------- CHANGE WORKING DIRECTORY:
# Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting.
import os
try:
	os.chdir(os.path.join(os.getcwd(), '/Users/pablodiaz/Downloads/l-dandy/work/t4-csv_to_db/db-populator-csv'))
	print(os.getcwd())
except:
	pass

# In[2]:

# -------------------------- IMPORT PACKAGES:
import pandas as pd
import psycopg2
import csv
import numpy as np
from psycopg2 import Error

# In[3]

# -------------------------- CONNECT TO POSTGRES DB:
try:
    connection = psycopg2.connect(user = "pablodiaz",
                                  password = "rootroot",
                                  host = "127.0.0.1",
                                  port = "5400",
                                  database = "DandyDB")
    cursor = connection.cursor()

    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

# In[4]

# -------------------------- CREATE TABLE
cursor.execute(''' DROP TABLE IF EXISTS "breed_supplement" ''');
connection.commit()
print("Table dropped successfully in PostgreSQL ")

try:
    create_table_query = '''CREATE TABLE "breed_supplement"
          (
          id SERIAL PRIMARY KEY,
          breed VARCHAR(80) NOT NULL,
          top_1_supplement VARCHAR(100),
          top_2_supplement VARCHAR(100),
          top_3_supplement VARCHAR(100),
          top_4_supplement VARCHAR(100),
          medical_issue_1 VARCHAR(100),
          medical_issue_2 VARCHAR(100),
          medical_issue_3 VARCHAR(100),
          medical_issue_4 VARCHAR(100)
          ); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)

# In[5]

# -------------------------- READ ALL CSV FILE (with pandas)
# uncoment line below
#csvFile = pd.read_csv('/Users/pablodiaz/Downloads/l-dandy/work/t4-csv_to_db/db-populator-csv/breed_supplement_matrix.csv')


# In[6]

# -------------------------- PRINT ALL CSV FILE (with pandas)
# uncoment line below
#csvFile

# In[7]

import csv
# -------------------------- READ CSV FILE (with csv)
# Importing data from csv file
f = open('/Users/pablodiaz/Downloads/l-dandy/work/t4-csv_to_db/db-populator-csv/breed_supplement_matrix.csv')
csvFile = csv.reader(f)

# In[8]

# -------------------------- INSERT ALL CSV ELEMENTS INTO DB
try:
    rowCount = 0
    for row in csvFile:
        print("----------------> In row: ")
        print(rowCount)

        #how many rows to insert:
        if rowCount == 100:
            break

        # --------- LOOP THROUGH ROW & append every element to cleared list
        elementsArr = []
        for element in row:
            print("==> every element: " + element)
            #if element is not None:
            #try:
            if element != '':
                elementsArr.append(element)
                print("-----> inside not None: " + element)
                #print(elementsArr)
            #else:
            #except:
            else:
                elementsArr.append("Null val")
                print("===========> 'None' type catch")

        # --------- print temporary list
        print("================> After for loop. list:")
        print(elementsArr)

        # --------- values to insert
        elem0 = elementsArr[0]
        elem1 = elementsArr[1]
        elem2 = elementsArr[2]
        elem3 = elementsArr[3]
        elem4 = elementsArr[4]
        elem9 = elementsArr[9]
        elem10 = elementsArr[10]
        elem11 = elementsArr[11]
        elem12 = elementsArr[12]
        
        print("----------------elem 0:")
        print(elem0)

        # --------- sql query
        sql_insert_query = """
            INSERT INTO "breed_supplement" (breed, top_1_supplement, top_2_supplement, top_3_supplement, top_4_supplement, medical_issue_1, medical_issue_2, medical_issue_3, medical_issue_4)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """ 
        record_to_insert = (elem0, elem1, elem2, elem3, elem4, elem9, elem10, elem11, elem12)
            #VALUES ('somethinng', 'elem1', 'elem2', 'elem3', 'elem4', 'elem9', 'elem10', 'elem11', 'elem12') """
            #VALUES (elementsArr[0], elementsArr[1], elementsArr[2], elementsArr[3], elementsArr[4], elementsArr[9], elementsArr[10], elementsArr[11], elementsArr[12]) """

        print("---------------->>>> AFTER INSERT")

        # --------- execute sql query
        cursor.execute(sql_insert_query, record_to_insert)

        print("--------------|--> AFTER CURSOR EXECUTE")

        # --------- commit
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into breed supplement table")

        # --------- clear array, display current row & increment row count
        elementsArr.clear()
        rowCount += 1
        print("----------||------> After commit")

# -------------------------- ERROR
except (Exception, psycopg2.Error) as error :
    #if(connection):
        print("Failed to insert record into breed_supplement table", error)
        #print("Failed inserting record into breed_supplement table {}".format(error))

# In[8.5]

# -------------------------- TEST ARRAY APPEND None VALUES:
row = ["1", "2", "", "4", "5", "6", "7"]
elementsArr = ["A", "b", "C", "d"]
#print(elementsArr)
for element in row:
    print("every element: " + element)
    #if not (element is None):
    #if element is not None:
    if element == "":
        print("not null: " + element)
        #elementsArr = elementsArr.append(element)
        #print(elementsArr)
    else:
        print("Empty element")


# In[9]

# -------------------------- TEST PRINT SPECIFIED CSV ELEMENTS
try:
    count = 0
    for row in csvFile:
        #print(row[1])
        #print(len(row))
        # how many rows to print:
        if count == 2:
            break
        for element in row:
            print(element)
        print("===========")
        count += 1
        #var elementCol_1 = row[0]

# -------------------------- ERROR
except (Exception, psycopg2.Error) as error :
    #if(connection):
        print("Failed to insert record into breed_supplement table", error)
        #print("Failed inserting record into breed_supplement table {}".format(error))

# In[10]

# -------------------------- TEST HARDCODED INSERT
try:
    # --------- sql query
    sql_insert_query = """ INSERT INTO "breed_supplement" (breed, top_1_supplement, top_2_supplement, top_3_supplement, top_4_supplement, medical_issue_1, medical_issue_2, medical_issue_3, medical_issue_4) VALUES ('shietsu', 'supplement one', 'supp two', 'supp 3', 'supp four', 'medical issue one', 'med issue 2', 'med 3', 'med 4') """
    #another_sql_query = """ INSERT INTO "breed_supplement" (breed, top_1_supplement, top_2_supplement, top_3_supplement, top_4_supplement, medical_issue_1, medical_issue_2, medical_issue_3, medical_issue_4) VALUES ('bull dog', 'supplement one', 'supp two', 'supp 3', 'supp four', 'medical issue one', 'med issue 2', 'med 3', 'med 4') """
    #record_to_insert = ('bull dog', 'magnesium', 'croquets')

    # --------- execute sql query
    cursor.execute(sql_insert_query)
    # --- executemany() to insert multiple rows rows
    #result = cursor.executemany(sql_insert_query, another_sql_query)
    #cursor.execute(postgres_insert_query, record_to_insert)

    # --------- commit
    connection.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into breed supplement table")

# -------------------------- ERROR
except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into breed_supplement table", error)
        #print("Failed inserting record into breed_supplement table {}".format(error))

# In[11]

# -------------------------- CLOSE DB CONNECTION
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
