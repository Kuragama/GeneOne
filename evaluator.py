__author__ = 'Evan'

from member import Member
import math

class Evaluator:

    def __init__(self):
        self.__MIN = 0
        self.__MAX = 20
        self.__BITS = 32

    def evaluate(self, member):
        x = self.binaryToNum(self.__MIN, self.__MAX, self.__BITS, member.chromosomes[0])
        #print("X:",x,"from",member.chromosomes[0])
        return 4 * x + math.sin(x) - math.cos(2 * x) - 0.2 * (x ** 2)
        #return math.sin(x) + 2 * math.cos(3 * x) + 3 * math.sin(2 * x) - 0.1 * x ** 2 + 0.05 * x ** 2.5
        #return math.sin(math.e ** x) + math.cos(x)
        #return -(x ** 2) + (3 * x) + 4
        #return math.sin(x) + (0.7 * x * math.cos(x) * math.sin(x ** 2))

    def numToBinary(self, bottom, top, precision, num):
        range = top - bottom
        num -= bottom
        #num/range = x/precision, num * precision = range * x
        return (num *(2 ** precision - 1)) / range

    def binaryToNum(self, bottom, top, precision, num):
        range = top - bottom
        return ((range * num) / (2 ** precision - 1)) + bottom

    def getBits(self):
        return self.__BITS