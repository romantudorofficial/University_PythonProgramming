# Homework 2 (Laboratory 3)



# Exercise 1

def fibonacci (n):

    fibonacci_list = []
    a, b = 0, 1

    for _ in range (n):
        fibonacci_list.append(a)
        a, b = b, a + b

    return fibonacci_list


def runExercise1 ():

    fibonacci_list = fibonacci(10)
    print("\n\tExercise 1:\n")
    print("The first 10 Fibonacci numbers are:\n")
    print(fibonacci_list)


runExercise1()



# Exercise 2

def is_prime (n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes (numbers):
    return [n for n in numbers if is_prime(n)]




def runExercise2 ():

    numbers = [20, 10, 50, 55, 54, 22, 10, 2, 5, 7]
    print("\n\tExercise 2:\n")
    print("The prime numbers are:\n")
    print(filter_primes(numbers))


runExercise2()



# Exercise 3

def list_operations (a, b):

    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))

    return (intersection, union, a_minus_b, b_minus_a)


def runExercise3 ():

    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]
    print("\n\tExercise 3:\n")
    result = list_operations(a, b)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("A - B:", result[2])
    print("B - A:", result[3])


runExercise3()



# Exercise 5

def zero_below_diagonal (matrix):

    n = len(matrix)

    for i in range (n):
        for j in range (i):
            matrix[i][j] = 0

    return matrix


def runExercise5 ():

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("\n\tExercise 5:\n")
    print(zero_below_diagonal(matrix))


runExercise5()



# Exercise 7

def is_palindrome (n):
    return str(n) == str(n)[::-1]


def palindrome_info (numbers):

    palindromes = [num for num in numbers if is_palindrome(num)]
    count_palindromes = len(palindromes)
    greatest_palindrome = max(palindromes) if palindromes else None

    return (count_palindromes, greatest_palindrome)


def runExercise7 ():

    numbers = [121, 131, 123, 989, 456, 101]
    result = palindrome_info(numbers)
    print("\n\tExercise 7:\n")
    print("Count of palindromes:", result[0])
    print("Greatest palindrome:", result[1])


runExercise7()