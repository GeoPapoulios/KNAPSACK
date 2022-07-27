import sys
import os
from numpy import *



#Checking arguments
if len(sys.argv)!=5 or not isinstance(int(sys.argv[1]),int) or not isinstance(int(sys.argv[2]),int) or not isinstance(int(sys.argv[3]),int) or not isinstance(int(sys.argv[4]),int):
    print('\n\nUsage:')
    print('<generator.py> <Number of Items> <Max weight> <Max Value> <Sack Capacity>')
    exit()

f = open("knapsack_"+sys.argv[1]+"_"+sys.argv[2]+"_"+sys.argv[3]+".txt", "w")
f.write(str(sys.argv[3]))
f.write('\n')
for x in range(int(sys.argv[1])): #creating an item with random value and random weight
    weight = random.randint(sys.argv[2])+1
    value =  random.randint(sys.argv[3])+1
    f.write(str(value)+" "+str(weight))
    f.write('\n')
f.close()