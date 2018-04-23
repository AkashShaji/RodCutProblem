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

def BottumCutRod(pricelist,n):
    r = [0] * (n+1)
    s = [0] * (n+1)
    for x in range(1,n+1):
        q = -math.inf
        for y in range(1,x+1):
            if q < pricelist[y-1] + r[x-y]:
                q = pricelist[y-1]+r[x-y]
                s[x] = y
        r[x] = q
    price = 0
    solution = []
    while(n > 0):
        solution.append(s[n])
        price+=pricelist[s[n]-1]
        n-=s[n]
    print(solution)
    print(price)

def topDownCutRod(pricelist,n):
    if(n == 0):
        return 0
    q = -math.inf
    for x in range (0,n):
        q = max(q,pricelist[x] + topDownCutRod(pricelist,n-x-1))
    print(q)
    return(q) 

def PrintCutRod(pricelist):
    for x in range(1,len(pricelist)+1):
        topDownCutRod(pricelist,x)
        BottumCutRod(pricelist,x)

