
# coding: utf-8

# ## Program to get all the characters in that message at positions that are present in the Fibonacci sequence

# In[1]:

from math import sqrt


# In[2]:

# message = "The Da Vinci Code is a 2003 mystery-detective novel by Dan Brown"


# ### Returns the fibonacci values of the given number
# e.g., fibo(10) --> 55.000000000000014

# In[3]:

def fibo(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


# ### Function that return the characters of message at fibonacci positions

# In[4]:

def FibonacciSecret(message):
    message = message.replace(' ', '')
    result = []
    for i in range(len(message)):
        result.append(message[int(fibo(i))].upper())
        if fibo(i + 1) > len(message):
            break
    return '-'.join(result)


# ### Get user inputs, 1 ≤ message.length ≤ 255

# In[5]:

while True:
    message = raw_input("Enter the message: ")
    if len(message) > 0 and len(message) <= 255:
        break
    else:
        print("Kindly enter a message between length 1 and 255")


# ### Call the function that returns our required results

# In[6]:

print FibonacciSecret(message)


# ### Calculate the time taken

# In[7]:

get_ipython().magic(u'timeit FibonacciSecret(message)')

