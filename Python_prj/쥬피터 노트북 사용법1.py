#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rd
n=15
for i in range(5):
    print(rd.randrange(n))


# In[2]:

get_ipython().run_line_magic('pinfo2', 'rd.choices')


# In[3]:


a=3


# In[4]:


b=5


# In[5]:


print(a+b)


# In[6]:


a+=2


# ###### eee
# ㅇㅇㅇㅇㅇ
# >ㅇㄹ
# dd
# 
# ddd
# >fff

# 😘😘😘😘😘😘😘😘😘
# >![ByeFeliciaHiGIF.gif](attachment:ByeFeliciaHiGIF.gif)

# >>>![BugsBunnyBunnyGIF.gif](attachment:BugsBunnyBunnyGIF.gif)

# ## 특
# 
# 1. ㅇ
# 1. ㅇㅇ
# 1. ㅇㅇㅇㅇㅇㅇ
# 1. ㅇㅇ
# 1. ㅇㅇㅇ
# 1. ㅇㅇ
# 1. ㅇㅇ

# ---
# 
# ## 시각화 ex1:그래프

# In[7]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
print("fig:", fig)
print("ax:", ax)


# In[8]:


get_ipython().run_line_magic('pinfo2', 'plt.subplots')


# In[9]:


import pandas as pd
import numpy as np
import matplotlib as mpl

df = pd.DataFrame({
    "strings": ["Adam", "Mike"],
    "ints": [1, 3],
    "floats": [1.123, 1000.23]
})
df.style \
  .format(precision=3, thousands=".", decimal=",") \
  .format_index(str.upper, axis=1) \
  .relabel_index(["row 1", "row 2"], axis=0)


# In[10]:


df = pd.DataFrame([[38.0, 2.0, 18.0, 22.0, 21, np.nan],[19, 439, 6, 452, 226,232]],
                  index=pd.Index(['Tumour (Positive)', 'Non-Tumour (Negative)'], name='Actual Label:'),
                  columns=pd.MultiIndex.from_product([['Decision Tree', 'Regression', 'Random'],['Tumour', 'Non-Tumour']], names=['Model:', 'Predicted:']))
df.style


# -----------------------
# # 사전 학습자료
# 
# - 다음 학슴 파이썬 기본편
# - 나도코딩 블로그(http://nadocoding.tistory.com)

# In[11]:


get_ipython().run_cell_magic('HTML', '', '<iframe width="300" height="200" src="https://www.youtube.com/embed/dJfq-eCi7KI" title="아나콘다 환경 설정 및 주피터 노트북 사용법" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>\n')


# In[12]:


import time
for i in range(10):
    print(i)
    time.sleep(1)


# %%
