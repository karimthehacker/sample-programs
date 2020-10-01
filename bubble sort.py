# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:42:44 2020

@author: Karim
"""

#sorting 
#bubble sort
#lst=[5,6,7,9,2,3,0,1,8,4]
def bubble(lst):
    for j in range(len(lst)):
        check_for_swap=False
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                swap=lst[i]
                lst[i]=lst[i+1]
                lst[i+1]=swap
                check_for_swap=True
            
        if check_for_swap==False:
            break
        print(lst)
    print(lst)
bubble([4,5,8,2,6])

