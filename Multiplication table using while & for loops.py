#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Multiplication table using while loop
n = 10
i = 1
while i <= n:
    j = 1
    while j <=n:
        print(j*i,end = '	') #which symbol ?
        j+=1
    print()
    i+=1


# In[3]:


#Multiplication table using for loop

n=int(input('Please enter a positive integer between 1 and 15: '))
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row*col, end = '	')
    print()

