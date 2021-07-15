#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT 3 : APPLY NORMALITY AND CORRELATION TESTS ON HOUSE PRICE FILE 
# # LECTURER: SIR TARIQ 
# # BY MUHAMMAD AMMAR JAMSHED 

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


data = pd.read_csv(r'C:\Users\muham\Downloads\house.csv')


# In[4]:


data


# In[5]:


data.dtypes


# # we first test all Gaussiann statistical methods which are normality testing methods which indictae whether the data is normally 
# # distributed and follows the bell curve nature of fluctuating at certain intervals and being 95% present within
# # the highest peak point

# In[7]:


# Shapiro (Normality test)
# we try to test whether the data of the 'Month Sold' has a gaussian distribution
from scipy.stats import shapiro 
data = data
stat, p = shapiro(data['MoSold'])
print('stat =%.3f, p = %.3f' % (stat, p))
if p > 0.05:
        print('Gaussian Probability')
else:
        print('Failed to get probability Gaussian')


# In[8]:


# Anderson Darling test (Normality test)
# we test whether the data of Lot Frontage is Gaussian
from scipy.stats import anderson
data = data
result = anderson(data['LotFrontage'])
print('stat =%.3f' % (result.statistic))
for i in range (len(result.critical_values)):
    sl,cv = result.significance_level[i], result.critical_values[i]
    print('stat=%.3f, p=%.3f' % (stat, p))
    if result.statistic < cv:
        print('probably Gaussian at the %.1f%% level' % (sl))
    else:
        print('probably Gaussian at the %.1f%% level' % (sl))


# In[9]:


#D^ Agostino's K^2 test Normality test
# we test whether the data of SalesPrice is Gaussian
from scipy.stats import normaltest
data_SP = data['SalePrice']
stat, p = normaltest(data_SP)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('probably Gaussian')
else:
    print('probably not gaussian')


# # we now will calculate correlation coeffecients between data sets from different columns 
# #to examine whether they are dependent or Independent events 
# # if the linear corrleation is acheived they are DEPENDENT events 
# # and vice versa

# In[10]:


# Pearson Correlation Coeffecient 
# we now test whether two sets of data from house prices have a relationship 
# We shall test whether SalePrice and LotArea have linear correlation
from scipy.stats import pearsonr
data_Sales_price = data['SalePrice']
data_LotArea = data['LotArea']
stat, p = pearsonr(data_Sales_price,data_LotArea)
print('stat=%.3f, p=%.3f' % (stat, p))
if p> 0.05:
    print('linear correlation has been achieved and they are DEPENDENT EVENTS')
else:
    print('Linear correlation is not achieved and they are INDEPENDENT EVENTS')


# In[11]:


# Spearmens Rank correlation test 
# we shall use Spearmen Rank correlation test to evelaute whether
# both data sets used have monotonic relationship or not
# WE SHALL TEST WHETHER SalePrince and MoSold have monotonic relationship in the direct or inverse direction
from scipy.stats import spearmanr 
data_sp_SR = data['SalePrice']
data_ms_SR = data['MoSold']
stat, p = spearmanr(data_sp_SR, data_ms_SR)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Spearmen Rank correlation has been achieved and they are DEPENDENT EVENTS')
else:
    print('Spearmen Rank correlation is not achieved and they are INDEPENDENT EVENTS')


# In[12]:


# Kendal Rank Coorelation test 
# we shall test whether whether MSSubClass and SalePrice have a monotonic relationship 
from scipy.stats import kendalltau
data_MSC = data['MSSubClass']
data_p = data['SalePrice']
stat, p = kendalltau(data_MSC, data_p)
print('stat=%.3f, p =%.3f' % (stat, p))
if p>0.05:
    print('Spearmen Rank correlation has been achieved and they are DEPENDENT EVENTS')
else:
    print('Spearmen Rank correlation is not achieved and they are INDEPENDENT EVENTS')


# In[13]:


# Chi-square test
# We shall test whether SalePrice and MSSubClass are dependent or independent events 
from scipy.stats import chi2_contingency
table = [data['MSSubClass'], data['SalePrice']]
stat, p, dof, expected = chi2_contingency(table)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('SalePrice and MSSubClass are Probably independent')
else:
	print('Probably dependent')


# In[ ]:




