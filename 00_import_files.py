# Databricks notebook source
#CONEXÃO COM O BANCO DE DADOS

host_name = 'dmbdataanalytics.database.windows.net'
port = 1433
database = 'dw'
user = 'diegobrasil'
password = 'qI&9q9goY63d'


# COMMAND ----------

#!pip3 install openpyxl
#!pip install xlrd
#!pip3 install --upgrade pandas

# COMMAND ----------

import pandas as pd
import os
#from pandas import ExcelFile

# COMMAND ----------

#filelocation = dbutils.fs.ls("dbfs:/FileStore/Base_2017.xlsx")
path = '/dbfs/FileStore'

files = os.listdir(path)
df = pd.DataFrame()

# COMMAND ----------

df = pd.read_excel(path, engine= 'openpyxl')

# COMMAND ----------

files_xlsx = [path+'/'+ f for f in files if f[-4:]=='xlsx']


# COMMAND ----------

for f in files_xlsx:
  data = pd.read_excel(f, engine= 'openpyxl')
  df = df.append(data)

# COMMAND ----------

from pyspark.sql import SparkSession
sparkDF=spark.createDataFrame(df) 


# COMMAND ----------

urlgrava = f'jdbc:sqlserver://{host_name}:{port};databaseName={database}'

sparkDF.write\
    .format("jdbc")\
    .mode("overwrite")\
    .option("truncate",True)\
    .option("url", urlgrava)\
    .option("dbtable", "stg.stg_vendas")\
    .option("user", user)\
    .option("password", password)\
    .save()


# COMMAND ----------



# COMMAND ----------


