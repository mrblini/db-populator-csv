#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# In[1]:
# Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '/Users/pablodiaz/Downloads/l-dandy/work/t4-csv_to_db/db-populator-csv'))
	print(os.getcwd())
except:
	pass


# In[2]:
import pandas as pd
import psycopg2
import numpy as np
from psycopg2 import Error


# In[3]:
# Importing data from csv file
Vet_Data = pd.read_csv('/Users/pablodiaz/Downloads/l-dandy/work/t4-csv_to_db/db-populator-csv/breed_supplement_matrix.csv')


#%%
Vet_Data


# In[5]

# -------------------------- CONNECT TO POSTGRES DB
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


# In[6]

# -------------------------- CREATE TABLE 
try:
    #create_table_query = '''CREATE TABLE breed_supplement
          #(breed_id INT PRIMARY KEY,
          #breed_type TEXT NOT NULL,
          #top_1_supplement TEXT,
          #top_2_supplement TEXT,
          #top_3_supplement TEXT,
          #top_4_supplement TEXT,
          #medical_issue_1 TEXT,
          #medical_issue_2 TEXT,
          #medical_issue_3 TEXT,
          #medical_issue_4 TEXT); '''
          
    create_table_query = '''CREATE TABLE "del"
          (id SERIAL PRIMARY KEY,
          dogType VARCHAR(80) NOT NULL,
          dogSupp VARCHAR(80),
          dogFood VARCHAR(80)); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")
    
except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)

    
# In[7]
    
# -------------------------- INSERT
try:
    #ALTER TABLE "del" ALTER COLUMN target
    
    # --------- sql query
    #postgres_insert_query = """ INSERT INTO breed_supplement (breed_type, top_1_supplement, top_2_supplement, top_3_supplement, top_4_supplement, medical_issue_1, medical_issue_2, medical_issue_3, medical_issue_4) VALUES ('eye supplement', 'hair supplement', 'liver supplement', 'heart supplement', 'eye fail', 'hair fail', 'liver fail', 'heart fail') """
    sql_insert_query = """ INSERT INTO "del" (dogType, dogSupp, dogFood) VALUES ('a shietsu', 'a supplement', 'some food') """
    another_sql_query = """ INSERT INTO "del" (dogType, dogSupp, dogFood) VALUES ('some shietsu', 'the supplement', 'the food') """
    #record_to_insert = ('bull dog', 'magnesium', 'croquets')

   
    # --------- execute sql query
    #cursor.execute(sql_insert_query)
    #cursor.execute(postgres_insert_query, record_to_insert)
    # --- executemany() to insert multiple rows rows
    result = cursor.executemany(sql_insert_query, another_sql_query)

    
    # --------- commit
    connection.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into breed supplement table")



# -------------------------- ERROR
except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into breed_supplement table", error)
        #print("Failed inserting record into mobile table {}".format(error))
        

# In[8]
        
# -------------------------- CLOSE DB CONNECTION 
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
#records_to_insert = [ (4,'LG', 800) , (5,'One Plus 6', 950)]
#bulkInsert(records_to_insert)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            