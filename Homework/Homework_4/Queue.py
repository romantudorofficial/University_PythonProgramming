"""
    Task 2 - Queue
"""



class Queue:

    def __init__ (self):

        """
            Initialize an empty queue.
        """

        self.queue = []


    def push (self, item):

        """
            Add an item to the end of the queue.
        """

        self.queue.append(item)


    def pop (self):

        """
            Remove and return the item from the front of the queue.
            Return None if the queue is empty.
        """

        if not self.queue:
            return None

        return self.queue.pop(0)


    def peek (self):

        """
            Return the front item of the queue without removing it.
            Return None if the queue is empty.
        """

        if not self.queue:
            return None

        return self.queue[0]


    def is_empty (self):

        """
            Check if the queue is empty.
        """

        return len(self.queue) == 0


    def size (self):

        """
            Return the number of items in the queue.
        """

        return len(self.queue)


    def __str__ (self):

        """
            Return a string representation of the queue.
        """

        return f"Queue({self.queue})"