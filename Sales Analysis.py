#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


sales_data = pd.read_csv('C:\Users\User\Desktop\US Sales.csv')


# In[4]:


sales_data = pd.read_csv('C:\\Users\\User\\Desktop\\US Sales.csv')


# In[5]:


print(sales_data.head())


# In[6]:


print(sales_data.isnull().sum())


# In[7]:


sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])


# In[8]:


sales_data['Month'] = sales_data['Order Date'].dt.month
sales_data['Hour'] = sales_data['Order Date'].dt.hour


# In[9]:


sales_data['Sales'] = sales_data['Quantity Ordered'] * sales_data['Price Each']


# In[10]:


monthly_sales = sales_data.groupby('Month')['Sales'].sum()


# In[11]:


hourly_orders = sales_data.groupby('Hour').size()


# In[12]:


best_selling_products = sales_data.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False).head(10)


# In[13]:


city_sales = sales_data.groupby('City')['Sales'].sum().sort_values(ascending=False)


# In[14]:


import matplotlib.pyplot as plt


# In[15]:


plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(range(1, 13))
plt.grid(True)
plt.show()


# In[16]:


plt.figure(figsize=(10, 6))
hourly_orders.plot(kind='bar', color='skyblue')
plt.title('Hourly Orders')
plt.xlabel('Hour')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()


# In[17]:


plt.figure(figsize=(10, 6))
best_selling_products.plot(kind='bar', color='lightgreen')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Product')
plt.ylabel('Quantity Ordered')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.show()


# In[18]:


plt.figure(figsize=(10, 6))
city_sales.plot(kind='bar', color='salmon')
plt.title('Sales by City')
plt.xlabel('City')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.show()


# In[ ]:




