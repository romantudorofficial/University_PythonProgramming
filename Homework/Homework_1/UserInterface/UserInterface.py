# User Interface

from Controller.Controller import runTask2
from Controller.Controller import runTask5
from Controller.Controller import runTask6
from Controller.Controller import runTask8



def runUserInterface ():

    printWelcomeMessage()
    task = int(getTask())
    interpretTask(task)



def printWelcomeMessage ():

    print("\n\tWelcome to Homework 1!")



def getTask ():

    return input("\n\tChoose a task: ")



def interpretTask (task):

    if task == 1:
        pass

    elif task == 2:

        text = input("\n\tWrite the text: ")
        result = runTask2(text)
        print("\n\tThe result is: " + str(result) + ".\n")

    elif task == 3:
        pass

    elif task == 4:
        pass

    elif task == 5:

        number = input("\n\tChoose a number: ")
        result = runTask5(number)
        if result == 1:
            print("\n\tThe number is palindrome.")
        else:
            print("\n\tThe number is not palindrome.")

    elif task == 6:

        text = input("\n\tWrite the text: ")
        result = runTask6(text)
        print("\n\tThe result is: " + str(result) + ".\n")

    elif task == 7:
        pass

    elif task == 8:

        text = input("\n\tWrite the text: ")
        result = runTask8(text)
        print("\n\tThe result is: " + str(result) + ".\n")

    else:

        print("\n\tThis task is not available. Please try again.")