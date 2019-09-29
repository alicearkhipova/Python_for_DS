#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np


# In[7]:


a = np.array ([[1,6],[2,8],[3,11],[3,10],[1,7]])


# In[8]:


a


# In[9]:



np.mean(a, axis = 0)


# In[10]:


mean_a=np.mean(a, axis = 0)


# In[11]:


mean_a


# In[12]:


a_centered = a - mean_a


# In[13]:


a_centered


# In[14]:


a[0,0]


# In[15]:


a[0,1]


# In[16]:


sp = a_centered[0,0]*a_centered[0,1]+a_centered[1,0]*a_centered[1,1]+a_centered[2,0]*a_centered[2,1]+a_centered[3,0]*a_centered[3,1]+a_centered[4,0]*a_centered[4,1]


# In[17]:


sp


# In[18]:


a_centered_sp = sp
sp


# In[19]:


a_centered_sp


# In[20]:


answer = a_centered_sp / 4
answer


# In[22]:


trans_a = a.transpose()


# In[23]:


trans_a


# In[24]:


get_ipython().run_line_magic('pinfo', 'cov')


# In[25]:


get_ipython().run_line_magic('pinfo', 'np.cov')


# In[26]:


c=np.cov(trans_a)


# In[27]:


c


# In[29]:


print(c[0,1])


# In[30]:


print('Hooraaaaay')


# In[ ]:




