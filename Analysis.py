import matplotlib.pyplot as plotter
import statistics
import EightQueens_1 as firstImplementation

MAIN_PATH = './Logs/'
PATH_BASIC = 'BasicImplementation/'
PATH_ENHANCED = 'EnhancedImplementation/'
PATH_BY_ITERATION = 'byIteration/'
PATH_BY_FITNESS = 'byFitness/'
EXECUTION_COUNT = 10

def runBasicAlgorithmIterations():

    executionFitness = []
    executionLog = open(MAIN_PATH + PATH_BASIC + PATH_BY_ITERATION + 'ExecutionByIteration_Data.txt', 'xt')
    for iterator in range(1,EXECUTION_COUNT + 1):
        print('Iterating...' + str(iterator))
        data = firstImplementation.runByIterations(1000)
        iterationFitness = []
        f = open(MAIN_PATH + PATH_BY_ITERATION + 'iteration_' + str(iterator) + '.txt', 'xt')
        f.write('Individuals:\n')

        for item in data:
            iterationFitness.append(item['fitness'])
            f.write('   ' + str(item) + '\n')

        iterationFitnessMean = statistics.mean(iterationFitness)
        iterationFitnessSTD = statistics.stdev(iterationFitness)

        f.write('Fitness Mean: ' + str(iterationFitnessMean) + '\n')
        f.write('Fitness STD: ' + str(iterationFitnessSTD) + '\n')
        f.close()

        executionFitness.append(iterationFitnessMean)
    
    plotSize = len(executionFitness)
    executionSTD = statistics.stdev(executionFitness)
    executionMean = statistics.mean(executionFitness)

    executionLog.write('Execution Fitness Mean: ' + str(executionMean) + '\n')
    executionLog.write('Execution Fitness STD: ' + str(executionSTD) + '\n')
    executionLog.close()

    plotter.bar([x for x in range(1,plotSize + 1)],executionFitness,color='green')
    plotter.errorbar([x for x in range(1,plotSize + 1)],executionFitness,executionSTD,ecolor='red')
    plotter.show()

def runBasicAlgorithmFitness():
    executionFitness = []
    executionLog = open(MAIN_PATH + PATH_BASIC + PATH_BY_FITNESS+ 'ExecutionByFitness_Data.txt', 'xt')
    for iterator in range(1,EXECUTION_COUNT + 1):
        print('Iterating...' + str(iterator))
        data = firstImplementation.runByFitness()
        iterationFitness = []
        f = open(MAIN_PATH + PATH_BY_FITNESS + 'iteration_' + str(iterator) + '.txt', 'xt')
        f.write('Individuals:\n')

        for item in data:
            iterationFitness.append(item['fitness'])
            f.write('   ' + str(item) + '\n')

        iterationFitnessMean = statistics.mean(iterationFitness)
        iterationFitnessSTD = statistics.stdev(iterationFitness)

        f.write('Fitness Mean: ' + str(iterationFitnessMean) + '\n')
        f.write('Fitness STD: ' + str(iterationFitnessSTD) + '\n')
        f.close()

        executionFitness.append(iterationFitnessMean)
    
    plotSize = len(executionFitness)
    executionSTD = statistics.stdev(executionFitness)
    executionMean = statistics.mean(executionFitness)

    executionLog.write('Execution Fitness Mean: ' + str(executionMean) + '\n')
    executionLog.write('Execution Fitness STD: ' + str(executionSTD) + '\n')
    executionLog.close()

    plotter.bar([x for x in range(1,plotSize + 1)],executionFitness,color='green')
    plotter.errorbar([x for x in range(1,plotSize + 1)],executionFitness,executionSTD,linestyle='None',ecolor='red')
    plotter.show()


def main():
    runBasicAlgorithmFitness()


main()
 