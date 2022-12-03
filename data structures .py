#!/usr/bin/env python
# coding: utf-8

# In[13]:


x=1
def convertion(x=1):
    y=x*0.99
    print("voici le prix en dollars:",y,"$")
    return y
    
r=convertion(1000)

print(r)


# In[32]:


x=1
o=20
def convertion(x=199):
    y=x*0.99
    return y

r=convertion()
r=r+(o*0.99)


# In[33]:


nb1=1
nb2=20
nb3=77
c=nb1+nb2+nb3
def convertion(c):
    y=c*0.99
    return y

convertion(c)


# In[34]:


#chepoint 3 
l=[2,3,6]
p=1
for e in l:
    p=p*e
    
print(p)


# In[40]:


#Question 2
l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
sorted(l,key=lambda X:X[1])


# In[42]:


#Question 4
{i+1:(i+1)**2 for i in range (8)}
    


# In[54]:


dt={}
d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
for k in d1.keys():
    dt[k]=d2.get(k,0)+d1[k]
    
    print(dt)


# In[69]:


def max3(a,b,c):
       if a>= b and a>=c:
           return a 
       elif b>=a and b>=c:
           return b
       else: 
         return c 
       
M=max3(20,35,19)
print(M)


# In[64]:


calculation = lambda a,b:(a+b, a-b) 
calculation(a=40,b=10)


# In[70]:


def somme(L):
    s=0
    for e in L:
        s=s+e
    return s

def multiplication(L):
    s=1
    for e in L:
        s=s*e 
    return s 


# In[72]:


#L=[5,6,9,1,8,4]
def ex3(L):
    L_pair=[L[i] for i in range(len(L)) if i%2==0]
    L_impair=[L[i] for i in range(len(L)) if i%2!=0]
    return(somme(l_pair), multiplacation(l_impair))


# In[77]:


#classes/oriented programming 
class person:
    def __init__(self,n,age):
        self.name=n
        self.age=age
        self.pos=(0,0)
        
    def __str__(self):
        return self.name + f"is {self.age} years old"
    
    #§del__slef_
    
    def speak(self,speech):
        print(self.name,":",speech)
    
    def skate(self):
        print(self.name,":","je suis entrain de faire du skate. ")
    
    def walk(self,direction)
        x,y=selg.position 
        if direction=="up";
            x+= 1
        elif direction== "down";
            x-= 1
        elif direction=="right";
            y+= 1
        elif direction== "left";
            y-= 1
        
        


# In[79]:


p=person("kenza",17)
p.skate()


# In[ ]:





# In[86]:


#matrix 
import numpy as np
new_array=np.array([[1,2,3],[4,5,6]])


# In[88]:


new_array[0]


# In[92]:


new_array[0,1]


# In[90]:


#peux generate un password 
new_array[:,1]


# In[93]:


new_array.size


# In[ ]:


#matrix
import numpy as np
a=np.zeros((4,2))
for i in range(a.shape[1]):
    a[:-1,i]= i+1
    a[a>0]-=1


# In[ ]:


A-A.mean(axia=1,keepdims=true)


# In[9]:


import pandas as pd 
ids=[3,4,5]
noms=["a","b","c"]

pd.Series(noms, index=ids)

# print(ids)  (condition, que les deux on la meme taille) 


# In[19]:


import pandas as pd 
ids=[3,4,5]
noms=["a","b","c"]

s1=pd.Series(ids, index=noms)
s2=pd.Series(noms, index=ids)


# In[13]:





# In[ ]:


ids2=[9,10,11]
noms2=["c","e","g"]

