import sys
import os
import numpy as np
import operator
import random
 
def parsing(filename):
    with open(filename) as f:
        nodes = []
        weights = []
        values = []
        capacity = int(f.readline().replace("\n",""))
        while(1):
            line = f.readline().replace("\n","")
            if line.strip()=="":
                break
            value,weight = line.split()
            weights.append(int(weight))
            values.append(int(value))
    return capacity,weights,values
    
  
def construction(values,weights,capacity,VW_table):
    picks = []
    picks_idx = []
    #GRASP
    i = 0
    evaluation = 0
    while i < len(values) and capacity != 0:
        if random.randint(0,20) > 18:
            lucky_intruder_id = random.randint(0,len(values)-1)
            if lucky_intruder_id in picks_idx or weights[VW_table[lucky_intruder_id][0]] > capacity:
                continue
            else:
                picks.append(VW_table[lucky_intruder_id][0])
                picks_idx.append(lucky_intruder_id)
                capacity -= weights[VW_table[lucky_intruder_id][0]]
                evaluation+=values[VW_table[lucky_intruder_id][0]]
                
        if weights[VW_table[i][0]] <= capacity and i not in picks_idx:
            picks.append(VW_table[i][0])
            picks_idx.append(i)
            capacity -= weights[VW_table[i][0]]
            evaluation+=values[VW_table[i][0]]
        i+=1   

    return picks,evaluation


    
#MAIN    
    
capacity, weights, values = parsing('knapsack_20_200_100.txt')

#creating Value/Weights table
# CELL [0] = INDEX, CELL [1] = V/W value
VW_table = []
for i in range(len(weights)):
    VW_table.append([i,values[i]/weights[i]]) 
VW_table.sort(key = operator.itemgetter(1),reverse=1)   
#producing construction heuristic with GRASP
picks,evaluation = construction(values,weights,capacity,VW_table)

#Writing down in file and in console
f = open('Output_File.txt','w')    
f.write(str(VW_table))
f.write("\n")
f.write("Picks:"+str(picks)+ "  Value:  "+str(evaluation))
f.write("\n")
f.write("A solution has been made using GRASP")
f.write("\n")
f.write("\n")

print("Picks:"+str(picks)+ "  Value:  "+str(evaluation))
print("A solution has been made using GRASP")

    
f.close()