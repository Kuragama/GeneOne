__author__ = 'Evan'

from member import Member
from evaluator import Evaluator
import random
import operator

class Population:

    def __init__(self, popSize=10, populate=False):
        self.__size = popSize
        self.__members = [None] * self.__size
        self.__eval = Evaluator()
        self.__BITS = self.__eval.getBits()
        if (populate):
            self.__populate(1, self.__BITS)

    def __populate(self, numChromosomes, numGenes, seed=-1):
        if (seed > 0):
            random.seed(seed)
        for i in range(self.__size):
            m = Member()
            for j in range(numChromosomes):
                m.chromosomes.append(random.randrange(0, 1 << numGenes))
                m.chromosomes.append(random.randrange(0, 1 << numGenes))
            self.__members[i] = m

    def nextGeneration(self):
        nextGen = self.__select()
        children = []
        for i in range(int(self.__size / 2)):
            p1 = random.randrange(len(nextGen))
            p2 = random.randrange(len(nextGen))
            while(p2 == p1):
                p2 = random.randrange(len(nextGen))
            m = self.crossover(nextGen[p1], nextGen[p2], random.randrange(self.__BITS - 1), self.__BITS)[1]
            if (random.randrange(10) == 0):
                #m.chromosomes[0] = self.mutate(m.chromosomes[0], random.randrange(self.__BITS))
                m = self.mutate(m, random.randrange(self.__BITS * len(m.chromosomes)), self.__BITS)
            children.append(m)
        self.__members = nextGen + children

    def __select(self):
        evals = {}
        for i in range(len(self.__members)):
            #print(self.__eval.evaluate(self.__members[i]))
            evals.update({i:self.__eval.evaluate(self.__members[i])})
        sort = sorted(evals.items(), key=operator.itemgetter(1))
        newPop = []
        for i in range(int(self.__size / 2)):
            newPop.append(self.__members[sort.pop()[0]])
        return newPop



    def crossover(self, m1, m2, radix, bits):
        # Convert all of the chromosomes in each member to a single binary number
        n1 = n2 = 0
        for i in range(len(m1.chromosomes)): # Each member should have the same number of chromosomes
            n1 += m1.chromosomes[i] * (2 ** (i * bits))
            n2 += m2.chromosomes[i] * (2 ** (i * bits))
        totalBits = bits * len(m1.chromosomes)
        if ((n1 > 2 ** totalBits) or (n2 > 2 ** totalBits)):
            return -1
        mask = (2 ** totalBits) - 1
        lm = mask >> totalBits - radix
        um = mask << radix
        cn1 = (n1 & lm) | (n2 & um)
        cn2 = (n1 & um) | (n2 & lm)
        # Convert back to members
        cm1 = Member()
        cm2 = Member()
        mask = (2 ** bits) - 1
        for i in range(len(m1.chromosomes)):
            cm1.chromosomes.append(cn1 & mask)
            cm2.chromosomes.append(cn2 & mask)
            cn1 >>= bits
            cn2 >>= bits
        return [cm1, cm2]

    def mutate(self, m, radix, bits):
        n = 0
        for i in range(len(m.chromosomes)): # Each member should have the same number of chromosomes
            n += m.chromosomes[i] * (2 ** (i * bits))
        mask = 2 ** radix
        if (n & mask == 0):
            n += mask
        else:
            n -= mask
        cm = Member()
        mask = (2 ** bits) - 1
        for i in range(len(m.chromosomes)):
            cm.chromosomes.append(n & mask)
            n >>= bits
        return cm

    def getSize(self):
        return self.__size

    def getMember(self, index):
        return self.__members[index]

    def setMember(self, index, member):
        if (member is Member):
            self.__members[index] = member

    def getEvaluator(self):
        return self.__eval

    def getBits(self):
        return self.__BITS

"""p = Population()
m1 = Member()
m1.chromosomes.append(255)
m1.chromosomes.append(255)
m2 = Member()
m2.chromosomes.append(0)
m2.chromosomes.append(0)
print(m1.chromosomes)
print(m2.chromosomes)
children = p.crossover(m1, m2, 11, 8)
print("Child One:",bin(children[0].chromosomes[0]),bin(children[0].chromosomes[1]))
print("Child Two: ",bin(children[1].chromosomes[0]), bin(children[1].chromosomes[1]))"""