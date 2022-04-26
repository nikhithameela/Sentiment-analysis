#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
review=pd.read_csv("C:/Users/Dell/OneDrive - purdue.edu/Mod 1/IT Project Managament/Group Project/reviews.csv")


# In[36]:


review=pd.read_csv("C:/Users/Dell/OneDrive - purdue.edu/Mod 1/IT Project Managament/Group Project/reviews.csv")
#train['review_id']=train.index
positive=pd.read_csv('C:/Users/Dell/OneDrive - purdue.edu/Mod 1/IT Project Managament/Group Project/positive-words.txt',header=None)
positive.columns=['words']
negative=pd.read_csv('C:/Users/Dell/OneDrive - purdue.edu/Mod 1/IT Project Managament/Group Project/negative-words.txt',header=None)
negative.columns=['words']
review=review.head(1000)
review.shape


# In[37]:


import re
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import *
stop_words=stopwords.words('english')


# In[38]:


stemmer = PorterStemmer()
#preprocess function 
stem_words=lambda x: stemmer.stem(x)
break_into_words = lambda x : re.findall("[a-zA-Z0-9]+", x)
skip_stop_words = lambda x: [w for w in x if w not in list(stop_words)]
skip_numeric = lambda x : [w for w in x if not w.isnumeric()]


# In[39]:


review['review']=review['comments'].astype(str)
review['review']=review['review'].str.lower()


# In[40]:


review['review2']=review['review'].apply(stem_words)
review['review2']=review['review2'].apply(break_into_words)
review['review2']=review['review2'].apply(skip_stop_words)
review['review2']=review['review2'].apply(skip_numeric)


# In[41]:



#count number of positive words
positive_words_count=review['review2'].map(lambda x: len([w for w in x if w in list(positive['words'])]))
#count number of negative words
negative_words_count=review['review2'].map(lambda x: len([w for w in x if w in list(negative['words'])]))
review['positive']=positive_words_count
review['negative']=negative_words_count


# In[46]:


dict_positive={}
for i in review['review2']:
    for j in i:
        if j in list(positive['words']):
            if j in dict_positive.keys():
                dict_positive[j]=dict_positive[j]+1
            else:
                dict_positive[j]=1
positive_df=pd.DataFrame(dict_positive,index=['Words','Count'])
positive_df1=positive_df.T
positive_df1['Words']=positive_df1.index
positive_df1.reset_index()
positive_df1.head()
positive_df1.shape
positive_df1.to_csv("C:/Users/Dell/OneDrive - purdue.edu/Mod 1/IT Project Managament/Group Project/positive_summary.csv")


# In[47]:


#Negative words
dict_negative={}
for i in review['review2']:
    for j in i:
        if j in list(negative['words']):
            if j in dict_negative.keys():
                dict_negative[j]=dict_negative[j]+1
            else:
                dict_negative[j]=1
negative_df=pd.DataFrame(dict_negative,index=['Words','Count'])
negative_df1=negative_df.T
negative_df1['Words']=negative_df1.index
negative_df1.head()
negative_df1.shape
negative_df1.to_csv("C:/Users/Dell/OneDrive - purdue.edu/Mod 1/IT Project Managament/Group Project/negative_summary.csv")


# In[11]:


final_df=review[['negative','positive','review','review2']]
final_df.head()
#final_df.to_csv("C:/Users/Dell/OneDrive - purdue.edu/Mod 1/IT Project Managament/Group Project/sample_review.csv")


# In[ ]:




