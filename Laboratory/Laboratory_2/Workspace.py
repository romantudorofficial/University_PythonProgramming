# Problem 1

def greatestCommmonDivisor (firstNumber, secondNumber):

    if (firstNumber == 0):
        return firstNumber
    if (secondNumber == 0):
        return secondNumber
    if (firstNumber == secondNumber):
        return firstNumber
    if (firstNumber > secondNumber):
        return greatestCommmonDivisor(firstNumber - secondNumber, secondNumber)
    return greatestCommmonDivisor(firstNumber, secondNumber - firstNumber)

def testGreatestCommmonDivisor ():
    firstNumber = 5
    secondNumber = 30
    print(greatestCommmonDivisor(firstNumber, secondNumber))

# testGreatestCommmonDivisor()



### Probleme Simple from vcraciun:

# Problem 1

a = 0b11110000 #binary
b = 0xF0          #
print(a)
print(str(bin(a)))
print(b)
print(hex(b))

def convert_10_2(nr):
    if nr == 0:
        return '0b0'

    result = ''

    while nr > 0:
        bit = nr % 2
        result = str(bit) + result
        nr = nr // 2

    return '0b' + result

print(convert_10_2(100), convert_10_2(1024))


# Problem 2

def convert_2_16(n):
    res = ''
    resturi = 0
    index = 0
    while (n):
        resturi += (n % 10) + (1 << index)
        index += 1
        n /= 10

    if index == 4 or not n:
        res += str(resturi) if resturi < 10 else chr(resturi - 10 + ord('A'))

    return res[::-1]

print(convert_2_16(1010), convert_2_16(1111), convert_2_16(10000))



# Problem 3



# Probleme complicate

# Problem 2

characters = "AEGIJ..."

num = 218553019
result = ''

while num > 0:

    remainder = num % 30
    result = characters[remainder] + result
    num //= 30

print(result)


# Problem 1

def group(n, nr_of_decimals):
    if len(str(n)) % 2 == 0:
        result = str(n) + '00' + nr_of_decimals
    else:
        result = '0' + str(n) + '00' + nr_of_decimals
    return result

def func (n, nr_of_decimals):
    groups = group(n, nr_of_decimals)
    print(groups)
    c = 0
    p = 0
    for index in range(len(groups)//2):
        c = c * 100 + groups[index * 2 : (index + 1) * 2]
        for i in range(10):
            if i*(20*p+i)>c:
                break
        i = i - 1
        y = i * (20 * p + i)
        p = p * 10 + i
        c -= y
    return p

func(52, 4)
func(152, 2)
print(func(2,3000))