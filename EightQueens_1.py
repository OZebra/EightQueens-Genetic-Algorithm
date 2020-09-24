import random

POPULATION_SIZE = 100
INDIVIDUAL_SIZE = 8

# 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000

def makeIndividual():
    individual =  [None] * INDIVIDUAL_SIZE
    #Adicionar (indSize + 1) no lugar do 9 pra fazer tabuleiros maiores
    for x in range(1,INDIVIDUAL_SIZE + 1):
        random.seed()
        index = random.randrange(0,INDIVIDUAL_SIZE)

        while individual[index] != None:
            index = random.randrange(0,INDIVIDUAL_SIZE)
        
        individual[index] = x

    return individual

def initPopulation(pop_size):
    popList = []

    for x in range(0,pop_size):
        popList.append({
            'genotype': makeIndividual(),
            'fitness': 0
        })

    return popList

def calculateColisions(gen):
    colisionCount = 0

    for index in range(0,len(gen)):
        for searchIndex in range(1,len(gen)):
            posIndex = index + searchIndex
            negIndex = index - searchIndex

            if negIndex >= 0:
                if abs(gen[index] - gen[negIndex]) == searchIndex:
                    colisionCount += 1

            if posIndex <= 7:
                if abs(gen[index] - gen[posIndex]) == searchIndex:
                    colisionCount += 1 

    return colisionCount/2
    

def calculateIndividualFitness(ind):
    genColisions = calculateColisions(ind['genotype'])

    ind['fitness'] = 1/(1+genColisions)

    return ind


def calculatePopulationFitness(pop):
    #Individual index
    for ind_index in range(0,len(pop)):
        pop[ind_index] = calculateIndividualFitness(pop[ind_index])

    return pop

def validatePopulation(pop):
    maxFitness = 0

    for individual in pop:
        if individual['fitness'] > maxFitness:
            maxFitness = individual['fitness']

    return maxFitness

def generateParents():


def cutAndCross(par):
    

def crossPopulation(pop):
    parents = generateParents()
    childs = cutAndCross(parents)

def main():

    population = initPopulation(POPULATION_SIZE)
    population = calculatePopulationFitness(population)

    iterations = 0

    while(validatePopulation(population) < 1 and iterations <= 1000):
        print('Iterating under the population! Iteration: ' + str(iterations))
    #    population = crossPopulation(population)
    #    population = filterPopulation(population)
    #    population = mutatePopulation(population)
    #    population = calculatePopulationFitness(population)
    #Printar a média de fitness, máximo e mínimo
        iterations += 1


    for individual in population:
        if individual['fitness'] == 1:
            print(individual)

main()