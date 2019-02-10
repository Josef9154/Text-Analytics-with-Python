#!/usr/bin/env python
# coding: utf-8

# # Joseph Rochelle
# # Week 8 Assignment

# In[21]:


def main():
    with open("gettysburg.txt", "r") as file_in:
        print(file_in.read())
main()


# In[25]:


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)


# In[23]:


for key in counts:
    print(key, counts[key])


# In[24]:


import string
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


# In[26]:


import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)


# In[ ]:




