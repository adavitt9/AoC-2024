# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:05:16 2024

@author: adam.davitt
"""

actual_in = [17639, 47 ,3858 ,0 ,470624 ,9467423 ,5 ,188]


mini_in = [125,17]

''' ---------------------------- PART 1 ------------------------------------ '''

my_in = actual_in
tot=0
for x in my_in:
    working=[x]
    for i in range(25):
        my_out=[]
        for a in working:
            if a==0:
                my_out+=[1]
            elif len(str(a))%2==0:
                b = len(str(a))//2
                my_out+=[int(str(a)[:b]),int(str(a)[b:])]
            else:
                my_out+=[a*2024]
        working=my_out[:]
    tot+=len(working)
        
                
        

''' ---------------------------- PART 2 ------------------------------------ '''

my_in = actual_in
tot=0
my_map={}
my_pop={}

for z in my_in:
    my_pop[z]=1

for i in range(75):
    inter_dict={}
    for a in my_pop.keys():
        if my_pop[a]>0:
            if a in my_map.keys():
                for c in my_map[a]:
                    if c in inter_dict.keys():
                        inter_dict[c]+=my_pop[a]
                    else:
                        inter_dict[c]=my_pop[a]
            else:
                if a==0:
                    out = [1]
                elif len(str(a))%2==0:
                    b = len(str(a))//2
                    out = [int(str(a)[:b]),int(str(a)[b:])]
                else:
                    out = [a * 2024]
                my_map[a]=out
                for d in out:
                    if d in inter_dict.keys():
                        inter_dict[d]+=my_pop[a]
                    else:
                        inter_dict[d]=my_pop[a]
            my_pop[a]=0
    for k in inter_dict.keys():
        my_pop[k] = inter_dict[k]
                    
print(sum(my_pop.values()))
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    