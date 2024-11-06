# Test


# Task 1

numbers = [(288, 399), (583, 192), (926, 697), (306, 254), (942, 730), (521, 680), (52, 602),
           (627, 647), (963, 607), (319, 138), (640, 701), (653, 966), (304, 764), (294, 65),
           (50, 597), (225, 254), (541, 847), (379, 273), (31, 36), (368, 993), (385, 243),
           (880, 241), (755, 451), (420, 554), (753, 927), (550, 142), (46, 168), (118, 156),
           (709, 217), (644, 606)]


def selectTuples (numbers):

    biggestNumbers = numbers

    print(biggestNumbers)


selectTuples(numbers)



# Task 2

l1 = [80,84,79,32,117,101]
l2 = [121,104,110,82,76,83]


generatedText = ""
for i, j in zip(l1, l2):
    generatedText = generatedText + chr(i) + chr(j)
print(generatedText)



# Task 3

print("###  #   # ##### #  #  ##  #   #\n"
      "#  #  # #    #   #  # #  # ##  #\n"
      "#  #  # #    #   #  # #  # ##  #\n"
      "###    #     #   #### #  # # # #\n"
      "#      #     #   #  # #  # #  ##\n"
      "#      #     #   #  # #  # #  ##\n"
      "#      #     #   #  #  ##  #   #\n")


line1 = 0b1110010010111110100100110010001
line2 = 0b1001001010000100010010100101001
line3 = 0b1001001010000100010010100101001
line4 = 0b1001001010000100010010100101001
line5 = 0b1001001010000100010010100101001
line6 = 0b1001001010000100010010100101001
line7 = 0b1001001010000100010010100101001

# print(line7)

# print(bin(1918847377)) + '\n' + str(bin(1229071657)) + '\n' + str(bin(1229071657)) + '\n' + str(bin(1229071657)) +
# '\n' + str(bin(1229071657)) + str(bin(1229071657)) + str(bin(1229071657))



# Task 4

def orderWords ():

    string = "Praslea a invins si cel de al treilea zmeu si eliberase si pe fata de imparat cea mai mica"
    sortedText = string.split()
    for word in sortedText:
        length = len(word)

    print(sortedText)

orderWords()



# Task 5

def getLastDigit (x, N):

    lastDigit = 0

    while N:
        x = x * x
        lastDigit = x % 10
        x = lastDigit
        N -= 1

    print(lastDigit)


getLastDigit(11, 3)