#!/usr/bin/env python
# coding: utf-8

# ## Question 1: Use yfinance to Extract Stock Data
# 
# #Reset the index, save, and display the first five rows of the tesla_data dataframe using the head function.
# #Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

# In[501]:


import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import re


# In[502]:


tsla = yf.Ticker("TSLA")


# In[503]:


tsla_data=tsla.history(period="max")
tsla_data.reset_index(inplace=True)
tsla_data.head(6)


# # #Question 2: Use Webscraping to Extract Tesla Revenue Data
# 
# Display the last five rows of the tesla_revenue dataframe using the tail function. Upload a screenshot of the results.

# In[554]:


url1="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data=requests.get(url1).text


# In[576]:


revenue=BeautifulSoup(html_data,"html.parser")
revenue_info= revenue.find_all("td")

dlist=rev_info[0::2]
revlist=rev_info[1::2]

newdlist=[]
newrevlist=[]
for i in dlist:
    date=i.text
    newdlist.append(date)
    newdlist=newdlist[0:98]
    
for i in revlist:
    a=(i.text)
    b=a.replace('$',"").replace(",","")
    revenue=pd.to_numeric(b,errors="coerce")
    newrevlist.append(revenue)
   
    
tsla_revenue=pd.DataFrame(index=range(98),columns=['Date' ,'Revenue'])
tsla_revenue['Date']=newdlist
tsla_revenue['Revenue']=newrevlist
tsla_revenue_df=gme_revenue.iloc[0:16,:]
tsla_revenue_df=gme_revenue_df.sort_values(by='Date')
tsla_revenue_df.tail()


# # Question 3: Use yfinance to Extract Stock Data
# 
# Reset the index, save, and display the first five rows of the gme_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

# In[506]:


gme = yf.Ticker("GME")


# In[507]:


gme_data=gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head(6)


# In[ ]:





# # Question 4: Use Webscraping to Extract GME Revenue Data
# 
# Display the last five rows of the gme_revenue dataframe using the tail function. Upload a screenshot of the results.
# 
# 

# In[508]:


url2="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data=requests.get(url2).text


# In[525]:


rev=BeautifulSoup(html_data,"html.parser")
rev_info= rev.find_all("td")
dlist=rev_info[0::2]
revlist=rev_info[1::2]

newdlist=[]
newrevlist=[]
for i in dlist:
    date=i.text
    newdlist.append(date)
    newdlist=newdlist[0:98]
    
for i in revlist:
    a=(i.text)
    b=a.replace('$',"").replace(",","")
    revenue=pd.to_numeric(b,errors="coerce")
    newrevlist.append(revenue)
       
gme_revenue=pd.DataFrame(index=range(98),columns=['Date' ,'Revenue'])
gme_revenue['Date']=newdlist
gme_revenue['Revenue']=newrevlist
gme_revenue_df=gme_revenue.iloc[0:16,:]
gme_revenue_df=gme_revenue_df.sort_values(by='Date')
gme_revenue_df.tail()


# # Question 5: Plot Tesla Stock Graph
# 
# Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph.
# 
# Upload a screenshot of your results.

# In[526]:


import matplotlib.pyplot as plt
x=tsla_data.Date
y=tsla_data.Open
plt.xlabel("Date")
plt.ylabel("Prices")


plt.plot(x,y)


# # Question 6: Plot GameStop Stock Graph
# 
# Use the make_graph function to graph the GameStop Stock Data, also provide a title for the graph.
# 
# Upload a screenshot of your results.

# In[527]:


import matplotlib.pyplot as plt
n=gme_revenue_df['Date']
z=gme_revenue_df['Revenue']
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.plot(n,z)


# In[ ]:





# In[ ]:




