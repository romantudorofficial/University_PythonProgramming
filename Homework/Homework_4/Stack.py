"""
    Task 1 - Stack
"""



class Stack:

    def __init__ (self):

        """
            Initialize an empty stack.
        """

        self.stack = []


    def push (self, item):

        """
            Add an item to the top of the stack.
        """

        self.stack.append(item)


    def pop (self):

        """
            Remove and return the top item from the stack.
            Return None if the stack is empty.
        """

        if not self.stack:
            return None

        return self.stack.pop()


    def peek (self):

        """
            Return the top item from the stack without removing it.
            Return None if the stack is empty.
        """

        if not self.stack:
            return None

        return self.stack[-1]


    def is_empty (self):

        """
            Check if the stack is empty.
        """

        return len(self.stack) == 0


    def size (self):

        """
            Return the number of items in the stack.
        """

        return len(self.stack)


    def __str__ (self):

        """
            Return a string representation of the stack.
        """

        return f"Stack({self.stack})"