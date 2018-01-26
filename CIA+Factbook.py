
# coding: utf-8

# In[5]:


import pandas as pd
import sqlite3

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
q1 = "SELECT * FROM sqlite_master where type=\"table\" "
cursor.execute(q1).fetchall()


# In[7]:


query1 = "SELECT * FROM sqlite_master WHERE type='table'"
pd.read_sql_query(query1, conn)


# In[8]:


query2 = "select * from facts limit 5"
pd.read_sql_query(query2, conn)


# In[9]:


query3 = '''
select min(population) minpop, max(population) maxpop, 
min(population_growth) minpopgrwth, max(population_growth) maxpopgrwth 
from facts
'''
pd.read_sql_query(query3, conn)


# In[12]:


query4 = '''
select *
from facts
where population == (select max(population) from facts)
'''

pd.read_sql_query(query4, conn)


# In[11]:


query5 = '''
select *
from facts
where population == (select min(population) from facts)
'''

pd.read_sql_query(query5, conn)


# In[23]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns

fig= plt.figure(figsize=(10,10))
ax= fig.add_subplot()

query6 = '''
select population, population_growth, birth_rate, death_rate
from facts
where population != (select max(population) from facts)
and population != (select min(population) from facts);
'''
pd.read_sql_query(query6 , conn).plot(ax)
pd.read_sql_query(query6 , conn).hist()


# In[27]:


query7 = "select name, cast(population as float)/cast(area as float) density from facts order by density desc limit 20"
pd.read_sql_query(query7, conn)


# In[28]:



query8 = '''select population, population_growth, birth_rate, death_rate
from facts
where population != (select max(population) from facts)
and population != (select min(population) from facts);
'''
pd.read_sql_query(query8, conn)

