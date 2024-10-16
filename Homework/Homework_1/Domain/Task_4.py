# Task 4



def convertString (string):

    for index in range (0, len(string)):
        if string[index].isupper():
            string[index].lower()

    return string