#!/usr/bin/env python
# coding: utf-8

# # TextBlob

# In[5]:


from textblob import TextBlob

text = "ByteTheWay is a 365 days challenge to learn new codes in an         easy way. Today, we learn to count the frequency of a certain         word. TextBlob is a library to process textual data [Natural         Language Processing - NLP]. NLP is a subfield of computers         science and artificial intelligence that allows computer to         understand text and spoken human language as well as humans do."

blob = TextBlob(text)
print(blob.word_counts['to'])


# TextBlob is a library to process textual data called Natural language Processing (NLP). NLP is a subfield of computer science and Artificial Intelligence (AI) that allows computers to understand text and spoken human language as well as humans do. Surprisingly, there is so many company that using this kind of AI to analyze what their customers think about their products these days! What do you think???

# In[ ]:




