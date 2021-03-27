#!/usr/bin/env python
# coding: utf-8

# In[1]:


#simple conversion pgms

amt = eval(input("Enter the amount : "))
dis = eval(input("Enter the discounted price :"))
dis_amt = (amt*dis)/100
print("The discounted price is : ",dis_amt)
finamt = amt - dis_amt
print("The final amount is : ",finamt)


# In[2]:


#grams to kg

gram = eval(input("Enter the value in grams : "))
print("The value is :", gram//1000, "kg and ", gram%1000, " grams")


# In[3]:


#km to mile claculation
km = eval(input("Enter the value in kilometers : "))
mile = km/1.609
#mile= km*0.62
print("The value is : " ,mile, " miles")


# In[4]:


#miles to km 
mile = eval(input("Enter the value in miles : "))
km = mile*1.609
print("The value is : ", km, " kms")

