#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# In[1]:
# Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '/Users/pablodiaz/Downloads/l-dandy/work/task3/db-populator-csv'))
	print(os.getcwd())
except:
	pass


# In[2]:
import pandas as pd
import numpy as np
psycopg2


# In[3]:
# Importing data from Vet Data
Vet_Data = pd.read_csv('/Users/pablodiaz/Downloads/l-dandy/work/task3/db-populator-csv/breed_supplement_matrix.csv')


# In[4]:
Vet_Data


#%%
# Connnect to postgress db
import psycopg2
try:
    connection = psycopg2.connect(user = "root",
                                  password = "rootroot",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "dandy_postgres_db")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

