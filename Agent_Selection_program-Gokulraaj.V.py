#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook

# In[ ]:


gokul = {
    "name": "gokul",
    'is_ava': 'yes',
    "ava_since": 8,
    "role":"sale"}
guru = {   
    "name": "guru",
    "is_ava": "yes",
    "ava_since": 8,
    "role":"speaker"}
hari = {    
    "name": "hari",
    "is_ava": "yes",
    "ava_since": 8,
    "role":"support"}
ashwin = {    
    "name": "ashwin",
    "is_ava": "yes",
    "ava_since": 8,
    "role":"sale"}
krishna = {    
    "name": "krishna",
    "is_ava": "yes",
    "ava_since": 8,
    "role":"support"}

issue = {
    "role":"empty",
    "duration":"empty",
    "need":"empty"}    

def all_avaliable():
    global issue
    global data
    for i in range (1,len(data)+1):
        if(data[i].get("role") == issue['role']):
            if(data[i].get("is_ava") == 'yes'):
                print(data[i],"\n")
                data[i]["is_ava"] = "no"
                time = int(data[i]["ava_since"])
                data[i]["ava_since"] = time + issue['duration']
                print(data[i],"\n")
                issue['need'] = issue['need'] - 1
                print(issue['need'])
            elif(data[i].get("is_ava") == 'no'):
                print("not avaliable",data[i]['name'])
        if(issue['need'] > 0):
            continue
        else:
            break

               
                    
def least_busy():
    global issue
    global data
    for i in range (len(data),0,-1):        
        if(data[i].get("role") == issue['role']):
            if(data[i].get("is_ava") == 'yes'):
                print(data[i],"\n")
                data[i]["is_ava"] = "no"
                time = int(data[i]["ava_since"])
                data[i]["ava_since"] = time + issue['duration']
                print(data[i],"\n")
                issue['need'] = issue['need'] - 1
                print(issue['need'])
            elif(data[i].get("is_ava") == 'no'):
                print("not avaliable",data[i]['name'])
        if(issue['need'] > 0):
            continue
        else:
            break
    
def random():
    global issue
    global data
    for i in range (1,len(data)+1):
        if(data[i].get("role") == issue['role']):
            if(data[i].get("is_ava") == 'yes'):
                print(data[i],"\n")
                data[i]["is_ava"] = "no"
                time = int(data[i]["ava_since"])
                data[i]["ava_since"] = time + issue['duration']
                print(data[i],"\n")
                issue['need'] = issue['need'] - 1
                print(issue['need'])
            elif(data[i].get("is_ava") == 'no'):
                print("not avaliable",data[i]['name'])
        if(issue['need'] > 0):
            continue
        else:
            break
            
            
def avaliblity_check():
    global data
    count = 0
    for i in range (1,len(data)+1,1):
        if(data[i].get('is_ava') == 'yes'):
            count= count+1
    print("avaliable employe:",count)
    if(count == 0):
        print("all busy")
    elif(count == 5):
        print("all avaliable")
        print("random")
    elif(count < 5 ):
        print("least busy")
    
    select = input("type the option bellow: ")
    if(select == "all avaliable"):
        all_avaliable()
    elif(select == "least busy"):
        least_busy()
    elif(select == "random"):
        random()
    
def issue_det():
    issue["role"] = str(input("enter the role of employee: "))
    issue["duration"] = int(input("enter the duraton needed: "))
    issue["need"] = int(input("enter the number of employe need: "))
    print(issue,"\n")
    avaliblity_check()   

def update_emp():
    global data
    x = input("enter employe name:")
    for i in range (1,len(data)+1):        
        if(data[i].get("name") == x ):
            print("changing avaliblity...")
            data[i]["is_ava"] = "yes"
            print("done")
            break
        continue
        
while 1:
    
    data = {1:gokul, 2:guru, 3:hari, 4:ashwin, 5:krishna }

    x = int(input("1.updat employe detail \n2.enter issue \n3.exit \n "))
             
    if(x == 1):
        update_emp()        
    elif(x == 2):
        issue_det()
    else:
        print("exit...")               

