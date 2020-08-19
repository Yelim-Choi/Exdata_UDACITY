#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


# In[3]:


df = pd.read_csv("C:/Users/yelim/Desktop/survey_results_public.csv", encoding = "ISO-8859-1")
schema = pd.read_csv("C:/Users/yelim/Desktop/survey_results_schema.csv")


# In[4]:


#### A Look at the Data
#### Solution to Question1

num_rows = df.shape[0]
num_cols = df.shape[1]

#### Solution to Question2

no_nulls = set(df.columns[df.isnull().mean()==0])

#### Solution to Question3

most_missing_cols = set(df.columns[df.isnull().mean()>0.75])

