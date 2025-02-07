import os
from src import knapsack_optimize as ko
import numpy as np
weights = np.array([114,23,112,33,47,50,100,330,110,90,170,125,170,35,45,210])
weight_limit = 1000
importance = np.array([20,32,44,13,10,50,60,30,120,150,60,24,45,100,20,310])
'''Genetic Algo parameters '''
pc= 0.8
pm = 0.2
generations =100
population =20
k = 4 #k  for K-way tournament selection
final_pop,list_obj = ko.optimize_knapsack(generations=generations, population=population,weights=weights,weight_limit=weight_limit,importance=importance,k=k,pc=pc,pm=pm)
print(f'\nObj: {max(list_obj)}\nWeight: {ko.fitness(final_pop[list_obj.index(max(list_obj))], weights)}\nFinal_pop: {final_pop[list_obj.index(max(list_obj))]}')
print(f"Only {100*population*generations/2**len(weights)}% sample space is explored to attain the optimal solution")