__author__ = 'Evan'

from population import Population
from member import Member
import random

POPULATION_SIZE = 100
MAX_GENERATIONS = 100

def initPopulation(size=-1):
    if (size != -1):
        population = Population(size, True)
    else:
        population = Population(populate=True)
    return population

population = initPopulation(POPULATION_SIZE)
for i in range(MAX_GENERATIONS):
    print("NEW GENERATION     GENERATION:",i)
    population.nextGeneration()
    sum = 0
    for j in range(population.getSize()):
        sum += population.getEvaluator().evaluate(population.getMember(j))
    print("GENERATION",i,"AVERAGE:",sum / POPULATION_SIZE)
for i in range(population.getSize()):
    print(population.getEvaluator().binaryToNum(-8,5,population.getBits(),population.getMember(i).chromosomes[0]),population.getEvaluator().binaryToNum(-8,5,population.getBits(),population.getMember(i).chromosomes[1]))
    print(population.getEvaluator().evaluate(population.getMember(i)))


