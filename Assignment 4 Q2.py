#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a Python program to triple all numbers of a given list of integers. Use Python map.


# In[7]:


nums = [1, 2, 3, 4, 5, 6, 7]
print("Sample list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of list numbers:")
print(list(result))


# In[ ]:




