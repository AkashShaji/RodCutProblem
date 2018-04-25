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

    print("price:" + str(price))
    print("cuts:" +str(solution))

def topDownCutRod(pricelist,n):
    print("price:" + str(topDownCutRodHelper(pricelist,n)))
    choices = []
    while(n > 0):
        q = -math.inf
        choice = -1
        for x in range(0,n):
            if(q <pricelist[x] + topDownCutRodHelper(pricelist,n-x-1)):
                choice = x
                q = max(q,pricelist[x] + topDownCutRodHelper(pricelist,n-x-1))
        choices.append(choice+1)
        n-=choice+1

    print("cuts:" +str( choices))

def topDownCutRodHelper(pricelist,n):
    if(n == 0):
        return 0
    q = -math.inf
    for x in range (0,n):
        q = max(q,pricelist[x] + topDownCutRodHelper(pricelist,n-x-1))
            
    return(q) 

def PrintCutRod(pricelist):
    for x in range(1,len(pricelist)+1):

        pl = pricelist.copy()
        start_time_topDownCutRod = time.clock()
        topDownCutRod(pl,x)
        end_time_topDownCutRod = time.clock()
        print("topDownCutRod CPU time (seconds): "+
            str(end_time_topDownCutRod - start_time_topDownCutRod))
        pl = pricelist.copy()
        start_time_BottumCutRod = time.clock()
        BottumCutRod(pl,x)
        end_time_BottumCutRod = time.clock()
        print("BottumCutRod CPU time (seconds): "+
                str(end_time_BottumCutRod - start_time_BottumCutRod))


