import random
import re

POPULATION_SIZE = 100
INDIVIDUAL_SIZE = 8
CANDIDATE_AMMOUNT = 5

MAX_CROSS_ITERATIONS = 10

ind_id = 0

def getID():
    global ind_id
    ind_id = ind_id + 1

    return ind_id - 1

def arrayToString(array):
    finalstring = ''
    for item in array:
        finalstring += format(item,'b').zfill(3) 

    return finalstring

def binaryToInt(string):
    return int(string, 2)

def stringToArray(string):
    array = re.findall('...', string)
    array = list(map(binaryToInt, array))
    return array

def makeIndividual():
    individual =  [None] * INDIVIDUAL_SIZE

    for x in range(0,INDIVIDUAL_SIZE):
        random.seed()
        index = random.randrange(0,INDIVIDUAL_SIZE)

        while individual[index] != None:
            index = random.randrange(0,INDIVIDUAL_SIZE)
        
        individual[index] = x

    return arrayToString(individual)

def initPopulation(pop_size):
    popList = []

    for x in range(0,pop_size):
        popList.append({
            'genotype': makeIndividual(),
            'fitness': 0,
            'id': getID()
        })

    return popList

def calculateColisions(genString):
    colisionCount = 0
    gen = stringToArray(genString)

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

    ind['fitness'] = 1/(1+(0.15*genColisions))

    return ind


def calculatePopulationFitness(pop):
    for ind_index in range(0,len(pop)):
        pop[ind_index] = calculateIndividualFitness(pop[ind_index])

    return pop

def validatePopulation(pop):
    maxFitness = 0

    for individual in pop:
        if individual['fitness'] > maxFitness:
            maxFitness = individual['fitness']

    return maxFitness

def getIndividualFitness(individual):
    return individual['fitness']

def selectParents(pop):
    parents = []
    parentsIds = []
    popLength = len(pop)

    for iterator in range(0,MAX_CROSS_ITERATIONS):
        parentsCandidates = []
        parentsCandidatesIds = []

        for index in range(0,CANDIDATE_AMMOUNT):
            random.seed()

            randIndex = random.randrange(0,popLength)

            while (pop[randIndex]['id'] in parentsIds) or (pop[randIndex]['id'] in parentsCandidatesIds):
                randIndex = random.randrange(0,popLength)

            parentsCandidates.append(pop[randIndex])
            parentsCandidatesIds.append(pop[randIndex]['id'])
        
        parentsCandidates.sort(key = getIndividualFitness)
        parent_1 = parentsCandidates.pop()
        parent_2 = parentsCandidates.pop()

        parentsIds.append(parent_1['id'])
        parentsIds.append(parent_2['id'])

        parents.append({
            "firstParent": parent_1,
            "secondParent": parent_2
        })

    return parents

def cutAndCross(par_1, par_2):
    gen_1 = stringToArray(par_1['genotype']);
    gen_2 = stringToArray(par_2['genotype']);

    crossGen = []

    crossOverControl = []

    for index in range(0,3):
        crossGen.append(gen_1[index])
        crossOverControl.append(gen_1[index]);
    
    for index in range(3,11):
        if(index < 8):
            if gen_2[index] not in crossOverControl:
                crossGen.append(gen_2[index]);
                crossOverControl.append(gen_2[index]);
        
        else:
            if(gen_2[index-8] not in crossOverControl):
                crossGen.append(gen_2[index - 8]);
                crossOverControl.append(gen_2[index-8]);

    return {
        'genotype': arrayToString(crossGen),
        'fitness': 0,
        'id': getID()
    }

def generateChildren(parents):
    generatedChildren = []

    for pair in parents:
        random.seed()
        shuffleChance = random.randrange(1,11);
        if(shuffleChance != 10):
            child_1 = cutAndCross(pair['firstParent'], pair['secondParent'])
            child_2 = cutAndCross(pair['secondParent'], pair['firstParent'])
        
        else:
            child_1 = pair['firstParent']
            child_2 = pair['secondParent']
        
        generatedChildren.append(child_1);
        generatedChildren.append(child_2);

    return generatedChildren

def mutate(individual):
    genAsArray = stringToArray(individual['genotype'])
    leng = int(len(genAsArray)/2)

    first = genAsArray[:leng]
    second = genAsArray[leng:]

    individual['genotype'] = arrayToString(first + second)

    return individual


def procreatePopulation(pop):
    parentsPairs = selectParents(pop)
    children = generateChildren(parentsPairs)
    childrenAmmount = len(children)
    
    for index in range(0,childrenAmmount):
        random.seed()
        roll = random.randrange(0,10)

        if roll < 4:
            children[index] = mutate(children[index])


    return pop + children

def filterPopulation(pop):
    newPopulation = calculatePopulationFitness(pop)
    newPopulation.sort(key = getIndividualFitness, reverse = True);

    populationOverflow = len(newPopulation) - 100

    while populationOverflow > 0:
        newPopulation.pop()
        populationOverflow -= 1

    return newPopulation

def printIndividuals(individuals):
    indLength = len(individuals)
    iterator = 1;

    for index in range(0, indLength):
        print(str(iterator) + ' - ', end='')
        print(individuals[index])

        iterator += 1

def runByIterations(iterationMax):
    population = initPopulation(POPULATION_SIZE)
    population = calculatePopulationFitness(population)

    iterations = 0

    while(iterations <= iterationMax):
        population = procreatePopulation(population)
        population = filterPopulation(population)

        iterations += 1

    return {
        'population': population,
        'iterationCount': iterations
    }
def runByFitness():

    population = initPopulation(POPULATION_SIZE)
    population = calculatePopulationFitness(population)

    iterator = 0

    while(validatePopulation(population) < 1 and iterator <= 1000):
        population = procreatePopulation(population)
        population = filterPopulation(population)
        iterator += 1

    print('Iteration count: ' + str(iterator))

    return {
        'population': population,
        'iterationCount': iterator
    }