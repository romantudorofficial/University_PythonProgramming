# Task 2



def getNumberOfVowels (string):

    vowels = "aeiouAEIOU"
    numberOfVowels = 0

    for letter in string:
        if vowels.find(letter) != -1:
            numberOfVowels += 1

    return numberOfVowels