"""
Copyright 2020 Qiaoyu Zhang
Version of python: Python 3.7
"""

"""
This module provides a object type called queue which uses the basic idea of a queue object and provides several methods
that normal queue has. Including: enqueue, dequeue, and isEmpty. 
"""


class Queue:
    """
    This object crates and provides all the methods of a queue.
    :argument: values(tuple)
    """
    def __init__(self, values):
        if type(values) == type(()):
            self.body = values
            self.length = len(self.body)
        elif type(values) == type([]):
            self.body = ()
            for element in values:
                self.body += (element,)
            self.length = len(self.body)

    def __str__(self):
        result = "Front: (  "
        for element in self.body:
            result += str(element) + "  "
        result += ")End"
        return result

    def enqueue(self, new):
        """
        Add an element to the end of the queue
        :argument: any type
        :return: None
        """
        self.length += 1
        self.body += (new, )

    def dequque(self):
        """
        Remove an element from the front of the queue
        :return: any type
        """
        temp = self.body[0]
        self.body = self.body[1:self.length]
        return temp

    def isEmpty(self):
        """
        Check if the queue is empty
        :return: Boolean values
        """
        if self.length == 0:
            return True
        else:
            return False


def main():
    test = (1,2,3)
    tests = Queue(test)
    print(tests)
    tests.enqueue(4)
    print(tests)
    print(tests.dequque())
    print(tests)


if __name__ == '__main__':
    main()
