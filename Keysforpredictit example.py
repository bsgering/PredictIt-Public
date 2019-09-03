#!/usr/bin/env python
# coding: utf-8

# In[17]:


import Keysforpredictit as ky
#import the Keysforpredictit python script as a "module" of sorts

fileList = ['2019-03-30.db', '2019-04-02.db'] #define the filelist here, I changed it so that you define the filelist
#in the analysis script rather than in the module, that way we get better usability if we want to ook at different
#db files


# In[18]:


marketIDsDNom = ky.pullMarkets('Who will win the 2020 Democratic presidential nomination?', fileList)
#pullmarkets takes (marketname, filelist), outputs a list of Market Key ID's
contractIDsDNom = ky.pullContract(marketIDsDNom, 'Joe Biden', fileList) 
#pullcontracts takes (marketids, contractname, filelist), outputs a list of contract IDs

print(contractIDsDNom, marketIDsDNom)


# In[ ]:




