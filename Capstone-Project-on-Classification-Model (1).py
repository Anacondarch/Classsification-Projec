#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st


# In[3]:


# getting the dataset in csv 
df = pd.read_csv(r"C:\Users\me\Desktop\water_potability.csv")
print (df)


# In[4]:


#  get the first five rows
df.head()


# In[5]:


# to get the first 12 rows 
df.head(12)


# In[6]:


#  Get the last 3000 rows
df.tail(3000)


# In[7]:


# try to determine the shape of the data e.g. number of rows and columns
df.shape


# In[8]:


#  know the information about the dataset
df.info()


# In[9]:


# get the null values present in the dataset
df.isnull().sum()


# In[10]:


# get the statistical info about the dataset
df.describe()


# In[11]:


# using loc to get the first two rows and columns 
df.loc[[0,1]]


# In[12]:


# getting the mode value of the specific column 'Sulfate'
st.mode(df.Sulfate)


# In[13]:


# Getting the mode value of the specfic column 'Trihalomethanes'
st.mode(df.Trihalomethanes)


# In[14]:


# Getting the mode value of the specfic columns 'ph'
st.mode(df.ph)


# In[15]:


# to access  the ph column and getting the first 12 values from the column
df['ph'].head(12)


# In[16]:


# using loc to get the three columns with the missing values
df.loc[[0,1],('ph','Sulfate','Trihalomethanes')]


# In[17]:


# to access the Sulfate column and the values 
df['Sulfate']


# In[18]:


# to access the column Trihalomethanes and the values
df['Trihalomethanes']


# In[19]:


# to  determine if there are outliers and to know the best imput method to fillna
fig,ax = plt.subplots(figsize =(10,6) )
sns.boxplot(df.Trihalomethanes)


# In[23]:


#linear graph
plt.plot(df.Sulfate, df.Conductivity)
plt.title('Conductivity against Sulfate')
plt.ylabel('Conductivity')
plt.xlabel('Sulfate')
plt.show()


# In[24]:


#histogram
 
waterplot = sns.jointplot(x= "Conductivity", y= "Sulfate", kind= "hist", palette= "bright", height=12, ratio=3, data=df)
 
plt.show()


# In[29]:


plt.plot(df.ph, df.Organic_carbon)
plt.title('Organic_carbon against PH')
plt.ylabel('Organic_carbon')
plt.xlabel('ph')
plt.show()


# In[30]:


plt.plot(df.Organic_carbon, df.Potability)
plt.title('Potability against Organic_carbon')
plt.ylabel('Potability')
plt.xlabel('Organic_carbon')
plt.show()


# In[34]:


sns.barplot(x= "Organic_carbon", y= "Potability", data=df, palette="bright")


# In[36]:


sns.barplot(x= "Organic_carbon", y= "Chloramines", data=df, palette="bright")


# In[38]:


sns.jointplot(x= "Organic_carbon", y= "Conductivity", data=df, palette="bright", kind = "hex")


# In[39]:


#histogram
waterplot = sns.jointplot(x= "Organic_carbon", y= "ph", kind= "hist", palette= "bright", height=12, ratio=3, data=df)
plt.show()


# In[ ]:




