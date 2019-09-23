#!/usr/bin/env python
# coding: utf-8

# In[18]:


import sqlalchemy as sql
import database_functions as db
import pandas as pd
from datetime import datetime, timedelta
import time


# In[21]:


def database_start():
    while True:
        database_name = datetime.now().strftime('%Y-%W')
        dataframe_insert = db.contractmakerfordb()
        engine = sql.create_engine('sqlite:///predictit_db_'+database_name+'.sqlite3', echo=False)
        dataframe_insert.to_sql('Contracts', con=engine, if_exists='append', index_label='id')
        engine.dispose()
        time.sleep(60)


# In[23]:


database_start()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




