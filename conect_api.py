# Databricks notebook source
!pip install geocoder

# COMMAND ----------

from datetime import datetime
import json
import pandas as pd
import geocoder
#import toml
import pandas as pd
#import spark as spark

# COMMAND ----------

env_APP_NAME = 'TwitterConnect'
env_API_KEY = 'EewAHJ5zL1NoNbOKgZU3dOrHw'
env_API_KEY_SECRET = '8DPojGo4JfUzw2eiorq3ySMnM7cBl5AuhVXuq5nP1hZYmJ7OMj'
env_ACCESS_TOKEN = '450974533-meCit0MAActH0oUmrdxvoBqmHnVtLBWydNZUCuN9'
env_ACCESS_TOKEN_SECRET = 'zzVjNddiC3zhVbkX9HV5LePz2mk8VnaDbcj1LiOvHOSNh'

# COMMAND ----------

!pip install TwitterSearch

# COMMAND ----------

#CONEXÃO COM O BANCO DE DADOS

host_name = 'dmbdataanalytics.database.windows.net'
port = 1433
database = 'dw'
user = 'diegobrasil'
password = 'qI&9q9goY63d'

url = f'jdbc:sqlserver://{host_name}:{port};databaseName={database};user={user};password={password}' 

# COMMAND ----------

qry = \
"""
select  
	ds_linha
from (
select 
	ds_linha,
	qtd_venda,
	ROW_NUMBER() OVER(ORDER BY qtd_venda desc) AS order_max 
from consume.tab_vendas_linha_anomes
where per_venda = '2019.12' ) vendas_linha
where order_max = 1
"""


dflinhas = spark.read\
.format('jdbc')\
.option('url', url)\
.option('query', qry)\
.load().toPandas()

# COMMAND ----------

Lista = dflinhas.values.tolist()
for line in Lista:
  tweets = []
  try:
      tso = TwitterSearchOrder() 
      tso.set_keywords(['Boticário',line[0]]) 
      tso.set_language('pt')
      tso.set_include_entities(False)

      ts = TwitterSearch(
          consumer_key = env_API_KEY,
          consumer_secret = env_API_KEY_SECRET,
          access_token = env_ACCESS_TOKEN,
          access_token_secret = env_ACCESS_TOKEN_SECRET
       )

      for tweet in ts.search_tweets_iterable(tso):
          data = {
                  'User' : tweet['user']['screen_name'],
                  'Texto' : tweet['text']
          } 
          tweets.append(data)
      df = pd.DataFrame(tweets)
  except TwitterSearchException as e: 
      print(e)

# COMMAND ----------

df.display()

# COMMAND ----------

sparkDF=spark.createDataFrame(df) 
sparkDF.write\
    .format("jdbc")\
    .mode("overwrite")\
    .option("truncate",True)\
    .option("url", url)\
    .option("dbtable", "consume.tab_twitterApi")\
    .option("user", user)\
    .option("password", password)\
    .save()

# COMMAND ----------



# COMMAND ----------


