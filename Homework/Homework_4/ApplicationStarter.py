"""
    Homework 4 (Laboratory 5)
"""

from Stack import Stack
from Queue import Queue
from Matrix import Matrix



# Task 1 - Stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print("Pop:", stack.pop())



# Task 2 - Queue

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print("Peek:", queue.peek())
print("Pop:", queue.pop())
print("Pop:", queue.pop())
print("Pop:", queue.pop())
print("Pop:", queue.pop())



# Task 3 - Matrix

matrix1 = Matrix(2, 3)
matrix1.set(0, 0, 1)
matrix1.set(0, 1, 2)
matrix1.set(0, 2, 3)
matrix1.set(1, 0, 4)
matrix1.set(1, 1, 5)
matrix1.set(1, 2, 6)

print("Matrix 1:")
print(matrix1)

print("\nTranspose of Matrix 1:")
transposed = matrix1.transpose()
print(transposed)

matrix1.apply(lambda x: x + 1)
print("\nMatrix 1 after applying lambda x + 1:")
print(matrix1)

matrix2 = Matrix(3, 2)
matrix2.set(0, 0, 7)
matrix2.set(0, 1, 8)
matrix2.set(1, 0, 9)
matrix2.set(1, 1, 10)
matrix2.set(2, 0, 11)
matrix2.set(2, 1, 12)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix 1 multiplied by Matrix 2:")
result = matrix1.multiply(matrix2)
print(result)