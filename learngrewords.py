
# coding: utf-8

# ### Flashcard Scheduling Algorithm

# In[37]:
savecount = 0
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import operator
from random import uniform
import time
import random
from time import sleep
import queue
from IPython.display import display, clear_output
from colorama import init, Fore, Back, Style
from PyDictionary import PyDictionary
dictionary=PyDictionary()
init(convert=True)


setwidth = "                                   "
for i in range(20):
    print(".")
def myprint(str1):
    mystring = str(str1)
    print(setwidth + mystring)
def myinput(str1):
    mystring = str(str1)
    x = input(setwidth + mystring)
    return x


# In[10]:


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#print(color.BOLD + color.PURPLE + 'Hello World !' + color.END)


# In[11]:


myprint(color.BOLD + "Starting in 3..." + color.END)
for i in range(3, -1, -1):
    clear_output(wait=True)
    sleep(0.75)
    myprint(i)



#words = pd.read_csv('myGREwords.csv', encoding="utf-8")
words = pd.read_csv('weightsGREwords.csv', encoding="utf-8").drop(['Unnamed: 0'], 1)


# In[12]:


words.head()


# In[13]:


len(words)


# In[14]:


prob = words["weight"]/sum(words["weight"])


# In[15]:


#if you remember the meaning, press y (yes), if not press n (no)
#every yes will decrement the weight column by -1, every no will give 3 * words["no"][i] 


# In[42]:
import json
mydictionary =  eval(open('dict.txt', 'r').read())

i_know = 'm'
count = 0
maxsize = 15
cache = []
while(i_know != 'x'):
    clear_output()
    index, value = max(enumerate(prob), key=operator.itemgetter(1))
    if (index in cache):
        index = random.randrange(len(words))
        value = prob[index]
    myprint("******************************")
    myprint(color.BOLD + color.YELLOW + words["words"][index] + color.END)
    myprint("******************************")
    myprint(color.BOLD + color.UNDERLINE + "press " + color.GREEN + "y if you know," + 
                   color.RED + " else press n" + color.END + " (or press x to exit):")
    i_know = myinput(":")
    new_weight = -1 
    if (i_know == 'n'):
        new_weight = 3 * words["no"][index] + 1
        words.loc[index, "no"] += 1
        words.loc[index, "weight"] += new_weight
    else:
        words.loc[index, "yes"] += 1
        words.loc[index, "weight"] += new_weight

#    thisword = dictionary.meaning(words["words"][index])
    thisword = mydictionary[words["words"][index]]
    if (thisword != None):
        for x in thisword:
            for i in range(len(thisword[x])):
                myprint(color.BOLD + thisword[x][i] + color.END)

    prob = words["weight"]/sum(words["weight"])
    savecount = savecount + 1
    if ((savecount % 20 == 0)):
        words.to_csv("weightsGREwords.csv")
        
    if (len(cache) == maxsize):
        cache.pop()
    cache.insert(0, index)
    sleep(0.3)


# In[29]:


words.to_csv("weightsGREwords.csv")

