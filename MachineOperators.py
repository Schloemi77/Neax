#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:43:46 2020

@author: timoschloemer
"""


def maintainMachine(machinesPerSite, C, P, first):
    
    counter = 0
    
    if (first):
        machinesPerSite -= C
    
    while (machinesPerSite > 0):
        machinesPerSite-=P
        counter += 1
    
    
    return int(counter) 

def getMachineOperator(machines, so_limit, mo_limit):

    machines = sorted(machines, reverse = True)


    machineOperator = 0
    for i in range(len(machines)):  
        machineOperator += maintainMachine(machines[i], so_limit, mo_limit, i==0)


    print('"machine_operators:"', machineOperator)
    
    
    
    
    

input1 = {
    "machines": [15,10],
    "C": 12,
    "P": 5
}



input2 = {
    "machines": [11,15, 13],
    "C": 9,
    "P": 5
}

input3 = {
    "machines": [22,15, 13, 11],
    "C": 12,
    "P": 5
}




getMachineOperator(input1['machines'], input1['C'], input1['P'])
getMachineOperator(input2['machines'], input2['C'], input2['P'])
getMachineOperator(input3['machines'], input3['C'], input3['P'])





