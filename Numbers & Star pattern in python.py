#!/usr/bin/env python
# coding: utf-8

# In[101]:


#Nested while
n = int(input("Enetr num"))
i=1
while i <=n:
    j=1
    while j <=n:
        print(j, end = " ")
        j+=1
    i+=1
    print()


# In[18]:


n = int(input("Enter num :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*", end = " ")
    print( )


# In[1]:


#Nested for loop

for i in range(6):
    for j in range(6):
        print(j, end= " ")
    print() # after printing 0-5 in 1st line this makes 2nd line    


# In[37]:


#number pattern using for() loop

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = ' ')
    print()
print()


# In[2]:


#for loop , taking input dynamically from the user
rows = int(input("Enter num. of rows :"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end = ' ')
    print()
print()


# In[76]:


#using while loop
n = int(input("Enter num"))
i = 1
while i <=n:
    j=1
    while j <= i:
        print(j, end = " ")
        j+=1
    i+=1
    print()


# In[29]:


# inverted half pyramid pattern with number
rows = 5
for i in range(rows, 0, -1):
   # print(" "* (10-i), end = " ")     for changing design
    for j in range(1, i + 1):
        print(j, end=' ')
    print("\r")


# In[31]:


#Number triangle pattern
#method 1
rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print("  ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
 
#########################
#method 2
for i in range(1,6):
    print("    " * (6-i-1), end = "  ")
    for j in range (1, i+1):
        print(j, end  = "  ")
    print( )
    


# In[37]:


# inverted half pyramid pattern with number
#METHOD 1

rows = 5 #initializing starting row numver as 5
for i in range(rows, 0, -1):
    print("  "* (5-i), end = " ")     #for changing design
    for j in range(1, i + 1):
        print(j, end='   ')   #space b/w numbers
    print("\r")

print( )
#METHOD 2
#directly taken starting point as 5
for i in range(5, 0, -1):
    print('  ' * (6 - i), end = '' '')  #spacing in the beginning chages whole pattern. 
    for j in range(1, i + 1):
        print( j , end = "  ")
    print()
print()


# In[54]:


#FOR LOOP
for i in range(1, 6): #static i/p
    print('  ' * (5 - i), end = "")
    for j in range(1, i + 1):
        print(j , end ="  ")
    print()
print()


# In[55]:


#using while loop taking i/p from user
n = int(input("Enter num"))
i = 1
while i <=n:
    print("  " * (20-i-1), end = "  ")
    j=1
    while j <= i:
        print(j, end = "  ")
        j+=1
    i+=1
    print()


# In[50]:


# inverted half pyramid pattern with number
rows = 5
for i in range(rows, 0, -1):
    print("    "* (5-i), end = " ")     #for changing design
    for j in range(1, i + 1):
        print(j, end='  ')
    print("\r")


# In[51]:


#for loop
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = ' ') # in place of j put "*" to print * pattern
    print()
print()


# In[24]:


rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')


# In[58]:


#Reverse number pattern
rows = 5
# reverse loop
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")


# In[13]:


for i in range(10,0,-1):
    for j in range(5,i-1):
        print(j, end = " ")
    print( )


# In[25]:


#inverted pyramid
rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')


# In[26]:


#Inverted Pyramid pattern with the same digit
rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")


# In[52]:


#Alternate numbers pattern using while loop
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')


# In[3]:


n = 5
i = 1
while i <= n:
    j = 1
    while j <= n:
        if j <= i:
            print(j,end = ' ')
        else:
            print("*",end = ' ')
        j+=1
    print()
    i+=1
print()


# In[69]:


n = 5
i = 1
while n >= i:
    j = 1
    while j <= 5:
        if j <= n:
            print(j,end = ' ')
        else:
            print("*",end = ' ')
        #print(j,end = ' ')
        j+=1
    print()
    n-=1  


# In[61]:


# * pattern using while loop
n = int(input("Enter num"))
i = 1
while i <=n:
    j=1
    while j <= i:
        print("*", end = " ")
        j+=1
    i+=1
    print()


# In[62]:


# * using for loop
# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")


# In[87]:


rows = 5
for j in range(1, rows+1):
    print(" *" * j)


# In[86]:


#Downward half-Pyramid Pattern of Star
rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")


# In[95]:


#Right start pattern of star
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


# In[98]:


#Left triangle pascal’s pattern
rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        # display space
        print('  ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows
while i >= 1:
    j = i
    while j <= rows:
        print('  ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1


# In[80]:


#Right triangle pyramid of Stars
# number of rows
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end="  ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print(" *", end=" ")
    print("")


# In[89]:


#Right down mirror star Pattern
rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1


# In[88]:


#Downward full Pyramid Pattern of star
rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")


# In[94]:


#Equilateral triangle pattern of star

print("Print equilateral triangle Pyramid using asterisk symbol ")
# printing full Triangle pyramid using stars
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end="  ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end='  ')
    print("  ")


# In[59]:


#SandClock pattern
for i in range(6, 1, -1):
    print('  ' * (7 - i), end = ' ')
    for j in range(1, i):
        print(j, end = '  ')
    print()
for i in range(2, 6):
    print('  ' * (7 - i), end = '')
    for j in range(1, i + 1):
        print(j, end = '  ')
    print()
print()


# In[99]:


#Sandglass pattern of star
rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1


# In[67]:


for i in range(1, 6):
    print('  ' * (7 - i), end =" ")
    for j in range(1, i + 1):
        print(j, end = '  ')
    print()
for i in range(5, 1, -1):
    print('  ' * (7 - i), end = '  ')
    for j in range(1, i):
        print(j, end = '  ')
    print()


# In[100]:


#Diamond-shaped pattern of stars
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")


# In[50]:


#Another diamond pattern of star
rows = 5
i = 1
while i <= rows:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i += 1

i = rows - 1
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k <= 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i -= 1


# In[49]:


#Heart

n = 6		
for row in range(0,n):
    for col in range(0,n+1):
        if(row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print('* ',end=' ')
        else:
            print('  ',end=' ')
              
    print()


# In[62]:


#Filled HEART

size = int(input("Enter the size of heart:"));print()
for i in range(size//2,size+1,2):
    for j in range(1,size-i,2):         #to print upper 2 pyramids
        print("",end=" ")
    for j in range(1,i+1):
        print("*",end="")
    for j in range(1,size-i+1):
        print("",end=" ")
    for j in range(1,i+1):
        print("*",end="")
    print()
#to print inverted pyramid
for i in range(size,0,-1):
    for j in range(i,size):
        print("",end=" ")
    for j in range(1,(i*2)):
        print("*",end="")
    print()


# In[63]:


size = int(input("Enter the size of heart:"));print()
for i in range(size//2,size+1,2):
    for j in range(1,size-i,2):         #to print upper 2 pyramids
        print("",end=" ")
    for j in range(1,i+1):
        print("*",end="")
    for j in range(1,size-i+1):
        print("",end=" ")
    for j in range(1,i+1):
        print("*",end="")
    print()


# In[7]:


n = 8
i = 1
while i <= n:
   j = 1
   while j <= n:
       if j == 1 or j == n or j == i:
           print("#",end = ' ')
       else:
           print(" ",end = ' ')
       j+=1
   print()
   i+=1
print()
i = 1
while i <= n:
   j = 1
   while j <= n:
       if i == 1 or j == 1 or i == n :
           print("#",end = ' ')
       else:
           print(" ",end = ' ')
       j+=1
   print()
   i+=1
print()
i = 1
while i <= n:
   j = 1
   while j <= n:
       if i == 1 or j == n or i == n or j == 1 or i == n//2:
           print("#",end = ' ')
       else:
           print("   ",end = ' ')
       j+=1
   print()
   i+=1


# In[9]:


#To print 'I'
n = 8
for i in range(1, n + 1):
    for j in range(1, n +1):
        if i == 1 or j == n//2 or i == n:
            print("#", end = ' ')
        else:
            print("   ", end = ' ')
        print(end = ' ')
    print()
print()


# In[11]:


#To print 'A'
n = 8
for i in range(1,n+1):
    for j in range(1,n+1):
        if ( i==1 or j==1 or j==n or i==n/2):
            print('#', end = " ")
        else:
            print(" ",end = '  ')
        print(end = ' ')
    print()
print()


# In[ ]:


#to print I, A using time module ---------------not working-------------dont copy
import time
n = int(input("Enter the range "))
for i in range(1,n+1):
    for j in range(1,n+1):
        time.sleep(0.1)
        if i==n or j==n//2 or i == 1:
            print("#", end = " ")
        else:
            print(" ", end= " ")
        print(" ")
        for j in range(1,n+1):
            time.sleep(0.1)
            if i==1 or j==1 or i == n//2 or i == n: # last 1 gottila
                 print("#", end = " ")
        else:
            print(" ", end= " ")
    print(" ")
            


# In[ ]:




