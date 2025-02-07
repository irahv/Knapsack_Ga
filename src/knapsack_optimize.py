import pandas as pd
import numpy as np
import random


def cross_over(mother,father,pc):
    if pc>float(np.random.uniform(0,1,1)):
        a = random.randint(0,len(mother))
        p1 = np.append(father[0:a],mother[a:len(mother)]) 
        p2 = np.append(mother[0:a],father[a:len(mother)]) 
    else:
        p1=mother
        p2=father
    return p1,p2


def mutate(array,pm):
    if pm>float(np.random.uniform(0,1,1)):
        a1 = array.copy()
        a = random.randint(0,len(a1)-1)
        if a1[a] ==1:
            a1[a] =0
        else:
            a1[a]=1
    else:
        a1=array.copy()
    return a1


def fitness(a,importance):
    return np.dot(a,importance)



def evaluator(a,weights,weight_limit):
    if np.dot(weights,a)<weight_limit:
        return 1
    else:
        return 0


def manipulate(pop,eval_list,weights,weight_limit):
    manipulate_list = [i for i in range(len(eval_list)) if eval_list[i]==0]
    for i in manipulate_list:
        pop[i]=np.random.randint(2,size=(1,len(weights)))
    eval_list = [evaluator(i,weights,weight_limit) for i in pop]
    if 0 in eval_list:
        # print('Recursive Manipulate')
        eval_list_if = eval_list.copy()
        return manipulate(pop.copy(),eval_list_if,weights,weight_limit)
    else:    
        return pop


def fitness_dict(pop,obj_val):
    pop_fitness_dict ={}
    for i in range(len(pop)):
        pop_fitness_dict.update({str(pop[i]):obj_val[i]})
    return pop_fitness_dict


def tournament_selection(pop,population_size,importance,k):
    pop_generation = np.zeros([population_size,len(importance)])
    for i in range(population_size):
        selection = random.sample(range(len(importance)),k)
        pop_sel = np.zeros([k,len(importance)])
        obj_pop_sel = []
        for j in range(len(selection)):
            pop_sel[j] =pop[selection[j]]   
            obj_pop_sel.append(fitness(pop[selection[j]],importance))
            pop_generation[i] = pop_sel[obj_pop_sel.index(max(obj_pop_sel))]
    return pop_generation

def optimize_knapsack(generations, population, weights, weight_limit,importance,k,pc,pm):
    for gen in range(generations):
        if gen ==0:
            
            pop = np.random.randint(2, size=(population, len(weights)))  
            eval_list = [evaluator(i,weights,weight_limit) for i in pop]
            
            if 0 in eval_list:
                pop=manipulate(pop.copy(),eval_list.copy(),weights.copy(),weight_limit)
            pop = tournament_selection(pop,population,importance,k)
            
        else:
            # print(f'Generation: {gen}')
            cross_pop = np.zeros([population,len(importance)])
            index = [i for i in range(len(pop)) if i%2==0]
            for i in index:
                a,b = cross_over(pop[i],pop[i+1],pc)
                cross_pop[i]=a
                cross_pop[i+1]=b
            eval_list = [evaluator(i,weights,weight_limit) for i in cross_pop]
            
            if 0 in eval_list:
                cross_pop = manipulate(cross_pop.copy(),eval_list.copy(),weights.copy(),weight_limit)
            mutate_pop = np.zeros([population,len(importance)])
            # print(mutate_pop)
                
            for i in range(population):
                mutate_pop[i] = mutate(cross_pop[i],pm)
            eval_list = [evaluator(i,weights,weight_limit) for i in mutate_pop]
            
            if 0 in eval_list:
                mutate_pop = manipulate(mutate_pop.copy(),eval_list.copy(),weights.copy(),weight_limit)
            pop = tournament_selection(mutate_pop.copy(),population,importance,k)
            #pop = mutate_pop.copy()
            list_obj=[]
            weight_list = []
            for i in range(len(pop)):
                list_obj.append(fitness(pop[i],importance))
                weight_list.append(fitness(pop[i],weights))
                
    return pop, list_obj 