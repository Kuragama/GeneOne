__author__ = 'Evan'

from member import Member

class Population:

    def crossover(m1, m2, radix, bits):
        # Convert all of the chromosomes in each member to a single binary number
        n1 = n2 = 0
        for i in range(len(m1.chromosomes)): # Each member should have the same number of chromosomes
            n1 += m1.chromosomes[i] * (2 ** i)
            n2 += m2.chromosomes[i] * (2 ** i)
        totalBits = bits * len(m1.chromosomes)
        if ((n1 > 2 ** totalBits) or (n2 > 2 ** totalBits)):
            return -1
        mask = (2 ** totalBits) - 1
        lm = mask >> totalBits - radix
        um = mask << totalBits
        print("lm:",bin(lm),"um:",bin(um))
        cn1 = (n1 & lm) | (n2 & um)
        cn2 = (n1 & um) | (n2 & lm)
        # Convert back to members
        cm1 = Member()
        cm2 = Member()
        mask = (2 ** bits) - 1
        for i in range(len(m1.chromosomes)):
            cm1.chromosomes.append(cn1 & mask)
            cm2.chromosomes.append(cn2 & mask)
            cm1 >> bits - 1
            cm2 >> bits - 1
        return [cm1, cm2]

    def mutate(n, radix):
        mask = 2 ** radix
        if (n & mask == 0):
            return (n + mask)
        else:
            return (n - mask)

p = Population()
m1 = Member()
m1.chromosomes.append(255)
m1.chromosomes.append(255)
m2 = Member()
m2.chromosomes.append(0)
m2.chromosomes.append(0)
children = p.crossover(m1, m2, 8, 8)
print("Child One:",bin(children[0].chromosomes))