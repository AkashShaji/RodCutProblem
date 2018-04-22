######################################################################################
#
#  Name:Akash Shaji
#  Date:4/20/18
#
#  This project compares two approaches to solving the cut rod problem.  A top down
#  approach and a bottom up approach.
#   
#
####################################################################################
import time
import random
import math

def topDownCutRod(pricelist,n):
    print ("cutting a rod of size " + str(n))
    print(pricelist)

def BottumCutRod(pricelist,n):
    if(n == 0):
        return 0
    q = -math.inf
    for x in range (1,n+1):
        q = max(q,pricelist[x] + BottumCutRod(pricelist,n-x))
    return(q) 

def PrintCutRod(pricelist):
    for x in range(1,len(pricelist)+1):
        topDownCutRod(pricelist,x)
        BottumCutRod(pricelist,x)

