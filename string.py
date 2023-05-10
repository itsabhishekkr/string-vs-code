#!/usr/bin/env python
# coding: utf-8

# # format is possible when string is attach with it if not then it occur error in your programm.

# In[13]:


w="welcome {} to {} wscubetech".format("hallo",40)
print(w)
a="ram {} to {} wscubetech".format("mannu","abhishek")

print(a)


# In[17]:


w="shivam is {} to {}".format("going","home")
print(w)


# ## on the basis of indexing

# In[21]:


a="ram is {0} not going to {1}".format("school","market")
print(a)
a="ram is {1} not going to {0}".format("school","market")
print(a)                                #index of school in format is 0 so it print when {0}
                                        #index of market in format is 1 so it print when {1}


# ## on the basis of element

# In[26]:


w="shivam is {a} to {b}".format(a=20,b=40)
print(w)
w="shivam is {b} to {a}".format(a="mohan",b=50)
print(w)


# ## how to get space.

# In[31]:


w="welcome {b:10} to {a} wscube".format(a=30,b=70)
print(w) #{b:10} means --------70 or 8space70
print(len(w))
print(w.find("7"))
print(w.index("7"))


# ## value place in between space{b:^10}

# In[32]:


w="welcome {b:^10} to {a} wscube".format(a=30,b=70)
print(w)


# ## value place in left side {b:<10}

# In[33]:


w="welcome {b:<10} to {a} wscube".format(a=30,b=70)
print(w)


# ## value place in right side {b:>10}

# In[34]:


w="welcome {b:>10} to {a} wscube".format(a=30,b=70)
print(w)


# In[ ]:




