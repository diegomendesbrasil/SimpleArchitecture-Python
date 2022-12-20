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

#TRANSFORMA EM LISTA O RESULTADO DA CONSULTA ANTERIOR
Lista = dflinhas.values.tolist()
Lista[0]

# COMMAND ----------

from TwitterSearch import *

tweets = []
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Boticário','MAQUIAGEM']) # let's define all words we would like to have a look for
    tso.set_language('pt') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = env_API_KEY,
        consumer_secret = env_API_KEY_SECRET,
        access_token = env_ACCESS_TOKEN,
        access_token_secret = env_ACCESS_TOKEN_SECRET
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        #criado dicionário para receber os valores
        data = {
                'User' : tweet['user']['screen_name'],
                'Texto' : tweet['text']
        } 
        tweets.append(data)
    df = pd.DataFrame(tweets)
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

# COMMAND ----------

df.display()

# COMMAND ----------

qry_Suite = \
"""
select  
	*
from
stg.stg_vendas
"""


TestCase = spark.read\
.format('jdbc')\
.option('url', url)\
.option('query', qry_Suite)\
.load().toPandas()

# COMMAND ----------



# COMMAND ----------


