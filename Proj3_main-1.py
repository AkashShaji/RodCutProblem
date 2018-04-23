######################################################################################
#     This is your main program that tests the classes you have written.
#
#      Here is the Rubric:
#
#       Write/test the bottom up rod cutting solution.  You must print out the
#       the full solution (optimal price and pieces used) otherwise, no points
#       will be given.  (35 points)
#
#       Write/test the top down rod cutting solution.   You must print out the
#       the full solution (optimal price and pieces used) otherwise, no points
#       will be given.  (35 points)
#
#       Compare the two approaches using two lists.  Name the lists price1.txt
#       and price2.txt. (5 points)
#
#       Time the approaches, and create Table 1 that shows the times in seconds for
#       all possible n in pricelist 1 and 2.  Add to your report. (5 points)
#
#       In your report, create Table 2 that shows the order of growth in Big O notation
#       for time and space for both algorithms. (5 points)
#
#       Create a user interface menu.
#           The user interface asks the user what pricelist to use (1 or 2)
#           and what size to cut the rod. (5 points)
#           There is also an option to run through all n and both pricelists at once (5 points)
#           This is in a loop.  The user has an option to quit. (5 points)
#
####################################################################################
import time
import random
from cutrodproblem import topDownCutRod, BottumCutRod, PrintCutRod



#files are formated such that the price for each size is in order, starting with 1

file1 = "price1.txt"
file2 = "price2.txt"

#need to change the template to read in two files that contain the 2 price lists.
#files are named price1.txt and price2.txt

#Create a User Inteface:
#In a loop, 
#The user is asked which pricelist(1 or 2) to use and what size to cut the rod (n).
#There is an option for the user to quit by entering q.
#If the user chooses an n larger than the pricelist can handle, the user is asked to try again.


#opening the files
pricelist1 = open(file1,"r")
pricelist1 = list(eval(pricelist1.read()))
pricelist2 = open(file2,"r")
pricelist2 = list(eval(pricelist2.read()))


#loop exit variable
userInput = -1
while userInput != "q":    
    userInput = -1
    while userInput != "1" and userInput != "2" and userInput != "3" and userInput !="q" :
        print("Welcome to the cutRod")
        print("Options:")
        print("1:Pricelist 1")
        print("2:Pricelist 2")
        print("3:Analyze both for all values")
        print("q:Quit")
        userInput = input(">>>")
    if userInput == "1" :
        n = int(input("Length of the rod \n>>>"))
        pricelist = pricelist1.copy()
        start_time_topDownCutRod = time.clock()
        topDownCutRod(pricelist,n)
        end_time_topDownCutRod = time.clock()
        print("topDownCutRod CPU time (seconds): "+
                str(end_time_topDownCutRod - start_time_topDownCutRod))

        pricelist = pricelist1.copy()
        start_time_BottumCutRod = time.clock()
        BottumCutRod(pricelist,n)
        end_time_BottumCutRod = time.clock()
        print("BottumCutRod CPU time (seconds): "+
                str(end_time_BottumCutRod - start_time_BottumCutRod))
        print(pricelist)
    elif userInput == "2" :
        n = int(input("Length of the rod \n>>>"))

        pricelist = pricelist2.copy()
        start_time_topDownCutRod = time.clock()
        topDownCutRod(pricelist,n)
        end_time_topDownCutRod = time.clock()
        print("topDownCutRod CPU time (seconds): "+
                str(end_time_topDownCutRod - start_time_topDownCutRod))

        pricelist = pricelist2.copy()
        start_time_BottumCutRod = time.clock()
        BottumCutRod(pricelist,n)
        end_time_BottumCutRod = time.clock()
        print("BottumCutRod CPU time (seconds): "+
                str(end_time_BottumCutRod - start_time_BottumCutRod))
        print(pricelist)
    elif userInput == "3":
        PrintCutRod(pricelist1)
        PrintCutRod(pricelist2)

    if userInput!="q":
        temp = input("Press enter to continue ")

    


