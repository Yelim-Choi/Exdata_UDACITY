#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ALookAtTheData as t
from IPython import display
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("C:/Users/yelim/Desktop/survey_results_public.csv", encoding = "ISO-8859-1")
schema = pd.read_csv("C:/Users/yelim/Desktop/survey_results_schema.csv")


# In[6]:


print(df.head(5), schema.head(5))


# As you work through the notebook in this and future parts of this program, you will see some consistencey in how to test your solutions to assure they match we achieved! In every environment, there is a solution file and a test file. There will be chekcs for each solution built into each notebook, but if you get stuck, you may also open the solution notebook to see how we find any of the solution. Let's look at an example.
# 
# ## Question 1
# 
# 1. provide the number of rows and clounms in this dataset.

# In[8]:


# We solved this one for you by providing the number of rows and columns :
# You can see how we are prompted that we solved for th number of rows and cols correctly!

num_rows = df.shape[0] #Provide the number of rows in the dataset
num_cols = schema.shape[1] #Provide the number of columns in the dataset

t.check_rows_cols(num_rows, num_cols)


# In[9]:


#If you want to more about what the test function is expecting,
#You can read the documentation the same way as any other function

get_ipython().run_line_magic('pinfo', 't.check_rows_cols')


# Now that you are familiar with how to test your code -

# ## Question2
# 
# 2. Which columns had no missing values? Provide a set of column names that have no missing values.

# In[23]:


no_nulls = set(df.columns[df.isnull().mean()==0])
t.no_null_cols(no_nulls)


# ## Question3
# 
# 3. Which columns have the most missing values? Provide a set of column name that have more than 75% if their values missing.

# In[31]:


most_missing_cols = set(df.columns[df.isnull().mean() > 0.75])#Provide a set of columns with more than 75% of the values missing

t.most_missing_cols(most_missing_cols)


# ### Question 4
# 
# **4.** Provide a pandas series of the different **Professional** status values in the dataset.  Store this pandas series in **status_vals**.  If you are correct, you should see a bar chart of the proportion of individuals in each status.

# In[30]:


status_vals = df.Professional.value_counts() #Provide a pandas series of the counts for each Professional status

# The below should be a bar chart of the proportion of individuals in each professional cateogry if your status_value
# is set up correctly

(status_vals/df.shape[0]).plot(kind="bar")
plt.title("What kind of developer are you?")


# ## Question5
# 
# **5.** Provide a pandas series of the different **FormalEducation** status values in the dataset.  Store this pandas series in **ed_vals**.  If you are correct, you should see a bar chart of the proportion of individuals in each status.

# In[33]:


ed_vals = df.FormalEducation.value_counts()#Provide a pandas series of the counts for each FormalEducation status

# The below should be a bar chart of the proportion of individuals in your ed_vals
# if it is set up correctly.

(ed_vals/df.shape[0]).plot(kind="bar");
plt.title("Formal Education");


# ## Question 6
# 
# **6.** Provide a pandas series of the different **Country** values in the dataset.  Store this pandas series in **count_vals**.  If you are correct, you should see a bar chart of the proportion of individuals in each country.

# In[34]:


count_vals = df.Country.value_counts()#Provide a pandas series of the counts for each Country

# The below should be a bar chart of the proportion of the top 10 countries for the
# individuals in your count_vals if it is set up correctly.

(count_vals[:10]/df.shape[0]).plot(kind="bar");
plt.title("Country");


# Feel free to explore the dataset further to gain additional familiarity with the columns and rows in the dataset. You will be working pretty closely with this datset throuhgout this lesson.

# In[35]:


pd.DataFrame(df.query("Professional == 'Professional developer' and (Gender == 'Male' or Gender == 'Female')")).groupby(['Gender','FormalEducation']).mean()['Salary']

