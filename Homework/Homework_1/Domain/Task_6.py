# Task 6



def getFirstNumber (text):

    number = 0

    for letter in text:
        if letter.isdigit():
            number = number * 10 + int(letter)
        if letter.isalpha() and number > 0:
            break

    return number