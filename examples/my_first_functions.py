#!/usr/bin/env python
# coding: utf-8

# ## My first Python Functions (modified 4/8)
# 
# added a few doctring examples """ docstring """
# 
# and some "magic" commands such as %%writefile

# In[ ]:


get_ipython().run_cell_magic('writefile', 'my_first_functions1.py', '\ndef the_weather():\n    """example with name defined non-local"""\n    print("Good morning " + name)\n    print("It\'s gonna be a hot one")')


# In[ ]:


name = "Vivian"


# In[ ]:


## later you can %run my_first_functions1.py
## recall the -i uses input from the notebook

get_ipython().run_line_magic('run', '-i my_first_functions1.py')

## also
## %run my_first_functions1.py "Vivian"`


# In[ ]:


the_weather()


# Silly example, yea, but demonstrates global, local, function definition

# In[ ]:


## BTW
get_ipython().run_line_magic('pycat', 'my_first_functions1.py')


# In[ ]:


# %load my_first_functions1.py

def the_weather():
    """example with name defined non-local"""
    print("Good morning " + name)
    print("It's gonna be a hot one")


# In[ ]:


def the_weather2():
    """example with name defined locally"""
    name = "Vivian Lew"  
    print("Good morning " + name)
    print("It's gonna be a hot one")


# In[ ]:


the_weather2()


# In[ ]:


print(name) # which one and why?


# We can pass a parameter between the parentheses, call it name, now can easily ues different values. Parameters store values.

# In[ ]:


def the_weather3(name):
    """example with name as parameter"""
    print("Good morning " + name)
    print("It's gonna be a hot one")


# In[ ]:


the_weather3("Vivian Lew")


# In[ ]:


the_weather3("UCLA")


# In[ ]:


the_weather3("everybody")


# How about something practical?  Can you program a square root function without importing a package?

# ## Returning a value

# In[ ]:


def tell_time(minutes):
    """example with return value"""
    estimate = str(minutes) +  " minutes left in class"
    return estimate


# In[ ]:


print(tell_time(15))

