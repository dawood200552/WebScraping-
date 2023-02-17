#!/usr/bin/env python
# coding: utf-8

# ## Question 1: Use yfinance to Extract Stock Data
# 
# #Reset the index, save, and display the first five rows of the tesla_data dataframe using the head function.
# #Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

# In[81]:


import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import re
import numpy as np


# In[82]:


tsla = yf.Ticker("TSLA")


# In[83]:


tsla_data=tsla.history(period="max")
tsla_data.reset_index(inplace=True)
tsla_data.head(6)


# # #Question 2: Use Webscraping to Extract Tesla Revenue Data
# 
# Display the last five rows of the tesla_revenue dataframe using the tail function. Upload a screenshot of the results.

# In[84]:


url1="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data=requests.get(url1).text


# In[85]:


containers=BeautifulSoup(html_data,"html.parser")
table = containers.find_all("table",{"class":"historical_data_table"})
info= table[1].find_all("tr")

date_list=[]
revenue_list=[]

for row in info:
    date =row.text.split("\n")[1]
    revenue = row.text.split("\n")[2].replace('$',"").replace(",","")
    date_list.append( date )
    revenue_list.append(revenue)
rev_df=pd.DataFrame({'Date':date_list, 'Revenue': revenue_list})
rev_df.drop([0],inplace=True)
table_df= rev_df.reset_index(drop=True).replace('',np.nan).dropna()
table_df.tail(6)
    


# In[86]:


import matplotlib.pyplot as plt
x=tsla_data.Date
y=tsla_data.Open

plt.xlabel("Date")
plt.ylabel("Prices")
plt.title('Open Prices')
plt.plot(x,y)


# In[87]:


r=table_df.Revenue.astype(int)
d=table_df.Date.sort_values(ascending=True)

plt.xlabel("Date")
plt.ylabel("Revenue")
plt.title('Tsla Revenue')
plt.plot(d,r)


# # Question 3: Use yfinance to Extract Stock Data
# 
# Reset the index, save, and display the first five rows of the gme_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

# In[88]:


gme = yf.Ticker("GME")


# In[89]:


gme_data=gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head(6)


# In[ ]:





# # Question 4: Use Webscraping to Extract GME Revenue Data
# 
# Display the last five rows of the gme_revenue dataframe using the tail function. Upload a screenshot of the results.
# 
# 

# In[90]:


url2="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data=requests.get(url2).text


# In[91]:


containers=BeautifulSoup(html_data,"html.parser")
table = containers.find_all("table",{"class":"historical_data_table"})
info= table[1].find_all("tr")

date_list=[]
revenue_list=[]

for row in info:
    date =row.text.split("\n")[1]
    revenue = row.text.split("\n")[2].replace("$","").replace(",","")
    date_list.append( date )
    revenue_list.append(revenue)
rev_df=pd.DataFrame({'Date':date_list, 'Revenue': revenue_list})
rev_df.drop([0],inplace=True)
table_df= rev_df.reset_index(drop=True).replace('',np.nan).dropna()
table_df.tail()
    


# In[ ]:





# In[ ]:





# # Question 5: Plot Tesla Stock Graph
# 
# Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph.
# 
# Upload a screenshot of your results.

# import matplotlib.pyplot as plt
# x=tsla_data.Date
# y=tsla_data.Open
# 
# plt.xlabel("Date")
# plt.ylabel("Prices")
# plt.title('Open Prices')
# plt.plot(x,y)
# 
# 

# r=table_df.Revenue.astype(int)
# d=table_df.Date
# 
# plt.xlabel("Date")
# plt.ylabel("Revenue")
# plt.title('Tsla Revenue')
# plt.plot(d,r)

# # Question 6: Plot GameStop Stock Graph
# 
# Use the make_graph function to graph the GameStop Stock Data, also provide a title for the graph.
# 
# Upload a screenshot of your results.

# In[92]:


import matplotlib.pyplot as plt
x=tsla_data.Date
y=tsla_data.Open

plt.xlabel("Date")
plt.ylabel("Prices")
plt.title('Open Prices')
plt.plot(x,y)


# In[93]:


r=table_df.Revenue.astype(int)
d=table_df.Date

plt.xlabel("Date")
plt.ylabel("Revenue")
plt.title('GME Revenue')
plt.plot(d,r)


# 

# In[ ]:




