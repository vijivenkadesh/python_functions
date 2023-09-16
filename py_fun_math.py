#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_range1(num1=0):
    '''This function sum all the numbers in the given range'''
    return sum(range(num1)) + num1


# In[58]:


def sum_range2(num1=0):
    '''This function sum all the numbers in the given range'''
    sum1 = 0
    for i in range(num1):
        sum1+=i
        sum2 = sum1 + num1
    return sum2


# In[ ]:




