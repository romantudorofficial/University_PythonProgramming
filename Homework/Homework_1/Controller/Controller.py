# Controller

from Domain.Task_2 import getNumberOfVowels
from Domain.Task_4 import convertString
from Domain.Task_5 import isPalindrome
from Domain.Task_6 import getFirstNumber
from Domain.Task_8 import getNumberOfWords



def runTask2 (string):

    return getNumberOfVowels(string)



def runTask4 (string):

    return convertString(string)



def runTask5 (number):

    return isPalindrome(number)



def runTask6 (text):

    return getFirstNumber(text)



def runTask8 (text):

    return getNumberOfWords(text)