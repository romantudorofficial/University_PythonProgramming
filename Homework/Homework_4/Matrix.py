"""
    Task 3 - Matrix
"""



class Matrix:

    def __init__ (self, n, m):

        """
            Initialize an N x M matrix filled with zeros.
        """

        self.rows = n
        self.cols = m
        self.data = [[0 for _ in range(m)] for _ in range(n)]


    def get (self, i, j):

        """
            Get the element at position (i, j).
        """

        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.data[i][j]
        else:
            raise IndexError("Index out of bounds")


    def set (self, i, j, value):

        """
            Set the element at position (i, j) to a specified value.
        """

        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.data[i][j] = value
        else:
            raise IndexError("Index out of bounds")


    def transpose (self):

        """
            Return the transpose of the matrix.
        """

        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))

        return transposed


    def multiply (self, other):

        """
            Multiply the current matrix by another matrix.
        """

        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not allow multiplication")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.get(i, k) * other.get(k, j) for k in range(self.cols))

        return result


    def apply (self, func):

        """
            Apply a lambda function to each element of the matrix.
        """

        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])


    def __str__ (self):

        """
            Return a string representation of the matrix.
        """

        return "\n".join(["\t".join(map(str, row)) for row in self.data])