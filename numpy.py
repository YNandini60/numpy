#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


np.__version__


# In[5]:


array1=np.array([1,2,3])
array1


# In[6]:


type(array1)


# In[54]:


arr2=np.array([
    [1,2],
    [3,4]
])
arr2


# In[8]:


arr2d=np.array([
    [1,2,3.3],
    [4,5,6.4]
])
arr2d


# In[10]:


arrex=np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])
arrex


# In[12]:


array3=np.array([
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [2,3,4],
        [10,11,12],
        [13,14,15]
    ]
])
array3


# In[15]:


array4=np.array((12,13,14))
array4


# In[19]:


print(array1.ndim)


# In[21]:


print(arr2d.ndim)


# In[24]:


print(array3.ndim)


# In[26]:


print(array4.ndim)


# In[28]:


array5=np.array([1,2,3,5],ndmin=4)
array5


# In[30]:


array5.shape


# In[32]:


array1.shape


# In[34]:


arr2d.shape


# In[36]:


array3.shape


# In[38]:


array4.shape


# In[40]:


arr2d


# In[41]:


arr2d[0][1]


# In[42]:


arr2d[1][0]


# In[47]:


arr2d[0][2]


# In[49]:


for x in range(0,2):
    for y in range(0,3):
        print(arr2d[x][y])


# In[51]:


array1.dtype


# In[55]:


arr2d.dtype


# In[58]:


array5=np.array([1,2,3,4,5],dtype='S')


# In[60]:


array5


# In[62]:


arr2d


# In[66]:


arr2dconv=arr2d.astype('i')
arr2dconv


# In[67]:


arr2dconv=arr2d.astype('f')
arr2dconv


# In[69]:


numone=np.ones((2,2),dtype=int)
numone


# In[71]:


num=np.ones(3)
num


# In[74]:


num3d=np.ones((2,3,3))
num3d


# In[76]:


numszero=np.zeros((2,3,3))
numszero


# In[78]:


numszero=np.zeros((3,2),dtype=int)
numszero


# In[79]:


range_array=np.arange(0,10,3)
range_array


# In[81]:


a=np.random.randint(low=1,size=5)
a


# In[83]:


b=np.random.randint(low=1,high=6,size=(2,3))
b


# In[86]:


np.concatenate([array1,array4])


# In[89]:


flatarr=array3.flatten()
flatarr


# In[91]:


np.reshape(flatarr[:4],(2,2))


# In[93]:


flatarr[:6]


# In[98]:


np.eye(5)


# In[100]:


np.eye(2,dtype=int)


# In[102]:


np.eye(5,dtype=int)


# In[103]:


import pandas as pd
df=pd.DataFrame(arr2d)
df

