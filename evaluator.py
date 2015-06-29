__author__ = 'Evan'

from member import Member
import math

class Evaluator:

    def __init__(self):
        self.__MIN = -8
        self.__MAX = 5
        self.__BITS = 32

    def evaluate(self, member):
        x = self.binaryToNum(self.__MIN, self.__MAX, self.__BITS, member.chromosomes[0])
        y = self.binaryToNum(self.__MIN, self.__MAX, self.__BITS, member.chromosomes[1])
        #print("X:",x,"from",member.chromosomes[0])
        return math.sin(x) - (y ** 2) / 10 - (x ** 2) / 10
        #return math.sin(x) + math.cos(y) + 0.1 * x * y

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