# Functionalities related to the OS, to interact with it, for example with files
# from os import * - we can also write it like this, so we don't have to write "os." in front of function calls
import os

import sys
import random

files = os.listdir('.')

def my_function (n):
    new_files = files
    print(new_files)

    s: int = 0
    # s = 0

    for i in range(1, n + 1):
        s += i
    return s


r = my_function(101)
print(r)




def summ(a, b):
    return a + b

v1 = summ(10, 20)
v2 = summ("abc", "xyz")
v3 = summ(4.5, 1.5)
print(v1, v2, v3)
#v4 = summ("abx")
#print(v4)   # this wont work



def my_function(n):
    s+=i
    return s

def summ(a, b):
    try:
        return a + b
    except:
        pass


def summ (a, b):
    if (type(a) is int or type(a) is float) and type(b) is str:
        return str(a) + b
    elif type(a) is str and (type(b) is int or type(b) is float):
        return  + str(b)
    else:
        return a + b



x = 1
if x == 1:
    print("something 1")
    print("something 2")
else:
    print("something 5")

for i in range(0, 10, 2):
#for i in range (10):
    print(i)

print("something 3")


for i in range (10):
    print(i, end = "",flush = True)

i = 0
while i < 10:
    print(i, end = "",flush = True)
    i += 1

print("\n")
print()


s = "My first string"
q = 65535
print("q is {1} and x is {0} and s is {2}".format(x, q, s))
print(f"{q} conversion to string is {hex(q)}\n{q} conversion to binary is {bin(q)}")      # f = formatted string


for i in range(10):
    print(f"{i:>04}", end = " ", flush = True)      #4 spaces, where i don't have digit i fill with 0 (also with "<", or without "0")


