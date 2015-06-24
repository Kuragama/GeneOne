__author__ = 'Evan'

from member import Member
import math

class Evaluator:

    def __init__(self):
        self.__MIN = -5
        self.__MAX = 5

    def evaluate(self, member):
        x = self.binaryToNum(self.__MIN, self.__MAX, 8, member.chromosomes[0])
        return math.sin(math.e ** x) + math.cos(x)
        #return -(x ** 2) + (3 * x) + 4
        #return math.sin(x) + (0.7 * x * math.cos(x) * math.sin(x ** 2))

    def numToBinary(self, bottom, top, precision, num):
        range = top - bottom
        num -= bottom
        #num/range = x/precision, num * precision = range * x
        return (num * precision) / range

    def binaryToNum(self, bottom, top, precision, num):
        range = top - bottom
        return ((range * num) / precision) + bottom