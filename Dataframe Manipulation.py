#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


superstore = pd.read_csv('/Users/luismoreira/Ironhack/Sample - EU Superstore.csv')
orders = pd.read_csv('/Users/luismoreira/Ironhack/orders.xlsx - orders.csv')


# In[4]:


pd.DataFrame(superstore)


# # Slicing in Datasets
# 

# In[18]:


# First rows
superstore.head()


# In[13]:


# Last Rows
superstore.tail()


# In[16]:


list(superstore.columns)


# In[20]:


# RENAMING COLUMNS
# you can use .columns to manually change the name of the columns

# e.g superstore.columns = ['Column ID','Order ID','Order Date','Ship Date', etc]
 
superstore.index


# In[22]:


list(superstore.index)


# In[24]:


superstore[['City', 'Country', 'Region']]


# # Basic exploration and computation

# In[26]:


# useful methods

superstore['Country'].nunique() # i.e. number of unique in column


# In[28]:


superstore['City'].unique()


# In[30]:


superstore['City'].value_counts()


# In[33]:


# Some useful column aggregations
# aggregation on all columns is the same as doing aggregations on the dataframe

superstore['Sales'].max() # sales with the highest value


# In[37]:


superstore[['Sales', 'Profit']].mean()


# In[39]:


superstore.mean()


# In[45]:


# we can do computation over oclumns

# unit price
superstore['Unitary price'] = superstore['Sales']/ superstore['Quantity']


# In[48]:


superstore[['Unitary price','Sales', 'Quantity']].head()


# In[51]:


# lets which orders have large sales

## T = 100 USD
 # create a boolean mask and save it
superstore['Large Sales'] = superstore['Sales'] > 100


# In[55]:


superstore[['Large Sales', 'Sales']].head


# In[61]:


superstore[superstore['Sales'] > 100] #  return th values in my dataframe where the condition stands true


# In[84]:


# do it yourself
# find me the order with maximum sales
order_max = superstore['Sales'].max()

# Or superstore.loc[superstore['Sales'] == order_max]

superstore[superstore['Sales'] == order_max]


# In[85]:


# boolean operators (and,or,not) which in pandas are denoted by (&, |, ~)

superstore['Large Quantity'] = superstore['Quantity'] > 5


# In[90]:


superstore['Large Sales'] = superstore['Sales'] > superstore['Sales'].mean()

superstore['Salesmean'] = superstore['Sales'].mean()

superstore[['Sales', 'Quantity', 'Salesmean', 'Large Sales', 'Large Quantity']].head()


# In[98]:


superstore['Large Quantity and Sale'] = (superstore['Quantity'] > 5) & (superstore['Sales'] > superstore['Sales'].mean())


# In[106]:


superstore['Large Quantity or Sales'] = (superstore['Quantity'] > 5) | (superstore['Sales'] > superstore['Sales'].mean())


# In[105]:


superstore['not Large Quantity'] = ~(superstore['Quantity'] > 5) # (superstore['Quantity'] <= 5)


# In[108]:


superstore[['Sales', 'Quantity', 'Salesmean', 'Large Sales', 'Large Quantity', 'Large Quantity and Sale', 'Large Quantity or Sales', 'not Large Quantity']].tail()


# In[114]:


condition = superstore['City'] == 'Lisbon'

superstore[condition]


# In[120]:


# combining boolean operators in filters

condition2 = (superstore['City'] == 'Lisbon') & (superstore['Segment'] == 'Corporate')

superstore[condition2]


# In[121]:


# interview question --> what condition returns more rows? condition and or condition or


# # Binning

# In[124]:


"""
< 0 --> 'Very Low'
0-200 --> 'Low'
201-500 --> 'Moderate'
501 - 1000 --> 'High'
>1000 --> 'Very High'
"""


# In[126]:


# cut method
my_labels = ['Very Low', 'Low','Moderate', 'High', 'Very High']
bins = pd.cut(superstore['Sales'], 5, labels = my_labels)

bins.value_counts()


# In[129]:


print(superstore['Sales'].min())
print(superstore['Sales'].max())

print('size of bins = ', (superstore['Sales'].max() - superstore['Sales'].min())/5)


# In[131]:


superstore.shape


# In[134]:


condition3 = superstore['Sales'] < 2.955 + 1591.125
superstore[condition3].shape


# In[136]:


condition4 = superstore['Sales'] > 7958.58 - 1591.125
superstore[condition4].shape


# In[137]:


# qcut

qbins = pd.qcut(superstore['Sales'], 5, labels = my_labels)
qbins.value_counts()

bins = pd.cut(superstore['Sales'], [0,10, 100, 1000, 2000, 6000], labels = my_labels)

import matplotlib


hist = superstore['Sales'].hist(bins = 5)

