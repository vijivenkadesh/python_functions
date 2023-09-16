#!/usr/bin/env python
# coding: utf-8

# In[40]:


def sum_range1(num=0):
    '''This function sum all the numbers in the given range'''
    num1 = int(input('Please enter the number range:'))
    return sum(range(num1)) + num1


# In[36]:


sum_range1()


# In[52]:


def sum_range2(num=0):
    '''This function sum all the numbers in the given range'''
    num1 = int(input('Please enter the number range:'))
    sum1 = 0
    for i in range(num1):
        sum1+=i
    return sum1


# In[ ]:




