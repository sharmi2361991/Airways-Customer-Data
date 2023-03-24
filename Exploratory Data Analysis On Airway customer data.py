#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports libaries


import pandas as pd
import numpy as np
import os

import datetime as dt

import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



# In[2]:


#get current working directory
cwd = os.getcwd()
#create a dataframe from csv file

df = pd.read_csv("airways customer data.csv")


# In[3]:


df.head()


# In[4]:


df['verified'] = df.reviews.str.contains("Trip Verified")


# In[5]:


df['verified']


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df.describe()


# In[9]:


df.info()


# In[10]:


#Cleaning/Format date
df.dtypes


# In[11]:


df.date = pd.to_datetime(df.date)


# In[12]:


df.date.head()


# In[13]:


#Cleaning ratings with stars
#check for unique values
df.rates.unique()


# In[14]:


# remove the \t and \n from the ratings
df.rates = df.rates.str.strip("\n\t\t\t\t\t\t\t\t\t\t\t\t\t")


# In[15]:


df.rates.value_counts()


# In[16]:


#There are 5 rows having values "None" in the ratings. We will drop all these 5 rows.
# drop the rows where the value of ratings is None
df.drop(df[df.rates == "None"].index, axis=0, inplace=True)


# In[17]:


#check the unique values again
df.rates.unique()


# In[18]:


#Check for null Values
df.isnull().value_counts()


# In[19]:


df.country.isnull().value_counts()


# In[20]:


#We have two missing values for country. For this we can just remove those two reviews (rows) from the dataframe
#drop the rows using index where the country value is null
df.drop(df[df.country.isnull() == True].index, axis=0, inplace=True)


# In[21]:


df.shape


# In[22]:


df.isnull().value_counts()


# In[23]:


#resetting the index
df.reset_index(drop=True)


# In[24]:


#What is the average overall rating given for British Airways?
df.rates.mean()


# In[25]:


df.rates.value_counts().plot(kind="bar")
plt.xlabel("Ratings")
plt.ylabel("Total Number of reviews with that rating")
plt.suptitle("Counts for each ratings")


# In[26]:


df_ratings = pd.DataFrame(df.rates.value_counts())
pct_values = (df_ratings.rates.values/ df_ratings.rates.values.sum() *100).tolist()
pct_values = [round(x,2) for x in pct_values]
df_ratings['pct_values'] = pct_values


# In[27]:


# renaming columns
df_ratings.rename(columns={'index':'rates', 'rates':'total_counts'}, inplace=True)


# In[28]:


df_ratings


# In[29]:


# Unique countries BA recieved the reviews from

print(f"{len(df.country.unique())} unique countries")


# In[30]:


#Which country most review comes from?
df_country_review = pd.DataFrame(df.country.value_counts().head()).reset_index()


# In[31]:


df_country_review.rename(columns={'index':'country','country':'total_reviews'}, inplace=True)


# In[32]:


df_country_review.plot(kind="bar", x='country')
plt.title("Maximum number of review by country")


# In[33]:


#convert the date datatype to datetime

df.date = pd.to_datetime(df.date)


# In[34]:


fig = px.line(df, x='date', y="rates")
fig.update_xaxes(rangeslider_visible=True)
fig.show()


# In[ ]:




