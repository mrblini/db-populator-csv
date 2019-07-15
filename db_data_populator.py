#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# In[1]:
# Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '/Users/pablodiaz/Downloads/l-dandy/work/t4-csv_to_db/db-populator-csv'))
	print(os.getcwd())
except:
	pass


# In[2]:
import pandas as pd
import numpy as np
import psycopg2
from psycopg2 import Error


# In[3]:
# Importing data from Vet Data
Vet_Data = pd.read_csv('/Users/pablodiaz/Downloads/l-dandy/work/t4-csv_to_db/db-populator-csv/breed_supplement_matrix.csv')


# In[4]:
Vet_Data


#%%
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
    
    
# -------------------------- CREATE TABLE 
    create_table_query = '''CREATE TABLE breed_supplement
          (breed_id INT PRIMARY KEY,
          breed_type TEXT NOT NULL,
          top_1_supplement TEXT,
          top_2_supplement TEXT,
          top_3_supplement TEXT,
          top_4_supplement TEXT,
          medical_issue_1 TEXT,
          medical_issue_2 TEXT,
          medical_issue_3 TEXT,
          medical_issue_4 TEXT); '''
          
    create_table_query = '''CREATE TABLE eraseMe
          (dogType TEXT,
          dogSupp TEXT,
          dogFood TEXT); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")
    
    
    # -------------------------- INSERT
    #postgres_insert_query = """ INSERT INTO breed_supplement (breed_type, top_1_supplement, top_2_supplement, top_3_supplement, top_4_supplement, medical_issue_1, medical_issue_2, medical_issue_3, medical_issue_4) VALUES ('eye supplement', 'hair supplement', 'liver supplement', 'heart supplement', 'eye fail', 'hair fail', 'liver fail', 'heart fail') """
    
    postgres_insert_query = """ INSERT INTO eraseMe (dogType, dogSupp, dogFood) VALUES ('golden ret', 'supplement', 'food') """
    
    record_to_insert = ('bull dog', 'magnesium', 'croquets')
    
    cursor.execute(postgres_insert_query, record_to_insert)
    
    #record_to_insert = ('new supplement record', 'another supplement', 'other supplement')
    #cursor.execute(postgres_insert_query, record_to_insert)
   
    #cursor.execute(postgres_insert_query)
    
    cursor.execute(record_to_insert)
    
    connection.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into mobile table")






# --------------------------
# -------------------------- ERROR
except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into breed_supplement table", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
# -------------------------- ERROR
#except (Exception, psycopg2.Error) as error :
    #print ("Error while connecting or inserting to PostgreSQL", error)
# ------- CLOSE CONNECTION 
#finally:
    #closing database connection.
        #if(connection):
            #cursor.close()
            #connection.close()
            #print("PostgreSQL connection is closed")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            