#!/usr/bin/env python
# coding: utf-8

# Introduction to Python in jupyter Notebook:
# 
# 
# pip - package installer for python
# 
# Jupyter Notebook is a web application that allows you to write and run Python programs in your browser rather than in the command line.
# Jupyter notebook keyboard shortcuts:
# Add a new cell and run the current one : Shift + Enter
# *esc brings the cell in command mode*
# to delete a cell : esc > d > d 
# to add cell below : esc > B
# to add cell below : esc > A
# to make the cell markdown, select the cell : esc > M 
# Markdown mode can contain text titles and even mathemtic equations.
# to aagin change the cell to code : esc > Y 
# to add title : # 
# smaller title : ## ; even smaller : ###

# ## Data Types in python 

# In[4]:


#defining variables(units that are assigned some value)
#should not start with numbers or use specia lcharacters in variable name 
#try not to start it with capital letter
x = 5


# In[5]:


#printing variables
print(x)


# In[6]:


#defining a string of characters
name = "Tanisha Lohchab"


# In[8]:


#to find the datatype of variable
#str for string
type(name)


# In[15]:


#adding two strings(concatinating the strings with arthemetic(addition) operator)

'strg1' + 'strg2'


# In[72]:


#list and strings are similar like slicing this can alsi=o be done for lists 
name[:4]


# In[74]:


#formatting a string
f"My name is {name}"


# In[75]:


import math
'Pi is: {}'.format(math.pi)


# In[77]:


#if you use three quotes '''...''' python goes in multiline string mode.

myString = '''
Here is a long block of text
I can add newlines!
the text doesn't stop until it sees \'\'\'

'''

print(myString)


# In[10]:


#defining a number(float or decimala , integers or whole numbers, complex numbers)
y = 0.0567
z = 123
q = 3j


# In[12]:


#check the type of each 
type(y)


# In[13]:


type(z)


# In[14]:


type(q)


# In[60]:


#to change the datatype of a variable in pytohn
int(100.453)


# In[62]:


#you can define the base of the number but then the n umber to be convereted should be a string
int('1ab', 16)


# In[64]:


#to round the decimal or floats
round(45.6)


# In[66]:


#the difference if you just convert it into int
int(45.6)


# In[16]:


#you can carry out several mathematical operations with these variables 
d = 1j + 1j


# In[32]:


#using the arthematic(modulus) operator - gives you the remainder of the division
z%y


# In[33]:


#exponential operator
3j ** 2


# In[17]:


print(d)


# In[18]:


#boolean  - True or False
#checking a condition with comparision operator(==, <=, >=, >, <)

1 == 3


# In[36]:


#using the logical operators (AND, OR, NOT)
True and True


# In[67]:


#casting Booleans
bool(1)


# In[68]:


bool(-2)


# In[69]:


bool(0)


# In[70]:


bool('anystringistrueexceptemptystring')


# In[71]:


#any empty datastructure or datatypes are False
bool("")


# In[ ]:


#byte object
#you can find modify detect and find bytes using the bytes() function.


# # Data Structures - Basics

# In[19]:


# LISTS
frst_list = [23, 1, 14, 56]


# In[20]:


print(frst_list)


# In[58]:


#accessing the one item from the list, index start from 0 to n-1; where n is the size of the list.
frst_list[2]


# In[21]:


listin_list = [['red','blue'], [1, 2, 3], 'reading', 345]


# In[38]:


#we can use the membership operator(in, not in) to check if the element is present in the list
345 in listin_list


# In[22]:


len(listin_list)


# In[25]:


#SETS : A set is almost identical to a list, except that all of the elements in it have to be unique. 
#Also, for lists order matters but for sets order doesnt matter.
#So we can define a set with curly brackets like this.

my_sets = {1, 323, 45, 6}
print(my_sets)


# In[26]:


#you can use the len() and type() functions as well
type(my_sets)


# In[27]:


#the lenght of the set is three becuase the number 11 is in repitetion
set1 = {11,11,23,3}
len(set1)


# In[28]:


print(set1)


# In[29]:


#TUPLES : similar to list but cannot new things cannot be added or appended and order does matter.
#(cannot modify a tuple so it is very memory efficient) used to store (x,y) cordinates 
tuple1 = (1, 2, 3)


# In[30]:


#DICTIONARIES : Has set of key and values. Keys has to be unique. It can store any datatypes as keys as well as values.

dict1 = { 'apple': 'lets go',
        'banana': 'big no'}


# In[31]:


#to access definition or the value of the key
dict1['apple']


# In[40]:


#the advantage of this method is it returns none if the key doesnt exists instead of an keyerror that the above method gives in similar case.
dict1.get('apple')


# In[41]:


dict1.get('notindict','key not found') #defining the value for key that doesnot exist


# In[42]:


#adding value in dictionary
dict1['pear'] = 'green fruit'


# In[43]:


print(dict1)


# In[48]:


#updating a value
dict1['pear'] = 'I am not afraid'


# In[45]:


print(dict1)


# In[46]:


#this both things can be done by using dict1.update() function it takes the dictionary of changes as argument
#delete a key from the dictionary
del dict1['pear']


# In[49]:


#we can also do this with pop() function, it also stores the value rather than just deleting it.
slogan1 = dict1.pop('pear')
print(slogan1)


# In[52]:


#looping through keys and values of dictionaries
dict1.keys()


# In[53]:


dict1.items()


# In[56]:


#looping through all the keys
for i in dict1:
    print(i)


# In[57]:


#looping through keys and values
for i,j in dict1.items():
    print(i,j)
    


# # Challenge 1

# In[59]:


#The Factorial Challenge:
# The factorial function gives the number of possible arrangements of a set of items of length "n"
# For example, there are 4! ("four factorial") or 24 ways to arrange four items, which can be calculated as: 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# etc.
# In a set of 0 items (an empty set) there is only one way to arrange the items, therefore, 0! = 1
# For the purposes of this exercise, factorials are only defined for positive integers (including 0)

# Returns the value of the factorial of num if it is defined, otherwise, returns None
def factorial(num):
    if type(num) == int and num >= 0:
        i = num
        fact = 1
        for i in range(num):
            if num == 0:
                fact = 1
            else:
                fact *= num
                num -= 1
        print(fact)
    else:
        print(None)
    


# # Challenge 2

# In[79]:


# #Converting Hexadecimal to Decimal
# Hexadecimal or "base 16" uses all of the numbers 0 - 9, plus a few others to signify higher numbers:
# A = 10
# B = 11
# C = 12
# D = 13
# E = 14
# F = 15
# Therefore, the number 'D' in hexadecimal would be 13 in decimal.
# The number '1A' in hexadecimal would be 26 in decimal. 
# Just like we have the "tens" place in base 10, hexadecimal has the "sixteens" place. 
# So 1A would be 16 + 10 or 26. 
# And just like decimal has the "hundreds" place (because 10 * 10 is 100), 
# hexadecimal has the "256's" place (because 16 * 16 is 256) 
# So 'ABC' in hexadecimal is (256 * 10) + (16 * 11) + (1 * 12) or 2,748

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    n = len(hexNum)
    decNum = 0
    for i in range(n):
        if hexNum[i] not in hexNumbers:
            print(None)
            return None
        else:
            decNum += (hexNumbers.get(hexNum[i]) * (16 ** (n-1 - i)))
    print(decNum)
            
           


# In[80]:


# 960
hexToDec('3C0')


# In[ ]:




