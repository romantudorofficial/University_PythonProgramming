# Homework 3 (Laboratory 4)



# Task 1

def getOperations (firstList, secondList):

    firstSet = set(firstList)
    secondSet = set(secondList)

    intersection = firstSet.intersection(secondSet)
    union = firstSet.union(secondSet)
    differenceFirstSecond = firstSet.difference(secondSet)
    differenceSecondFirst = secondSet.difference(firstSet)

    return [intersection, union, differenceFirstSecond, differenceSecondFirst]


def testGetOperations ():

    firstList = [1, 2, 3, 4]
    secondList = [3, 4, 5, 6]
    result = getOperations(firstList, secondList)
    print(result)


testGetOperations()



# Task 2

def countCharacters (text):

    counter = {}

    for char in text:
        counter[char] = counter.get(char, 0) + 1

    return counter


def testCountCharacters ():

    text = "Ana has apples."
    result = countCharacters(text)
    print(result)


testCountCharacters()



# Task 4

def buildXmlElement (tag, content, **attributes):

    attributesString = ' '.join(f'{key}="{value}"' for key, value in attributes.items())
    xmlElement = f"<{tag} {attributesString}>{content}</{tag}>"

    return xmlElement


def testBuildXmlElement ():

    result = buildXmlElement("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
    print(result)


testBuildXmlElement()



# Task 6

def countUniqueAndDuplicates (elements):

    uniqueElements = set()
    duplicateElements = set()

    for item in elements:
        if item in uniqueElements:
            duplicateElements.add(item)
        else:
            uniqueElements.add(item)

    numberOfUnique = len(uniqueElements - duplicateElements)
    numberOfDuplicates = len(duplicateElements)

    return numberOfUnique, numberOfDuplicates


def testCountUniqueAndDuplicates ():

    sampleList = [1, 2, 2, 2, 2, 3, 4, 4, 4, 5]
    result = countUniqueAndDuplicates(sampleList)
    print(result)


testCountUniqueAndDuplicates()