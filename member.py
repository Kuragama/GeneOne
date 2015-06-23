__author__ = 'Evan'

class Member:
    chromosomes = []

    def numToBinary(bottom, top, precision, num):
        range = top - bottom
        num -= bottom
        #num/range = x/precision, num * precision = range * x
        return (num * precision) / range

    def binaryToNum(bottom, top, precision, num):
        range = top - bottom
        return ((range * num) / precision) + bottom


"""i = -8.0

while(i <= 8.0):
    result = int(numToBinary(-8, 8, 1024, i))
    print(i,"   ",result,bin(result),"   ",binaryToNum(-8, 8, 1024, result))
    i += (16/1024)

# Demonstrating random crossovers
n1 = 0
n2 = 255
children = crossover(n1, n2, 7, 8)
print(n1,bin(n1),n2,bin(n2))
print(children[0],bin(children[0]),children[1],bin(children[1]))

# Demonstrating random mutations
print(mutate(255, 7))"""
