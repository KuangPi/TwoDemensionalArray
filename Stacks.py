import sys
"""
Copyright 2020 Qiaoyu Zhang
Version of python: Python 3.7
"""

"""
This module provides a object type called stack which has the methods of an usual stack. The data is not changeable for
the ones at the bottom of the stacks. The top data could be push, pop, peek. For the whole stack, it could be print and
check if it is empty. 
Also a interesting object type called sentence was occured. I didn't write description for it. You could test run the 
function and try the result XD. 
"""


class Stack:
    """
    This object crates and provides all the methods of a stack.
    :argument: values(tuple)
    """
    def __init__(self, values):
        assert type(values) == type(())
        self.body = values
        self.length = len(self.body)

    def __str__(self):
        result = "(\n"
        for element in self.body:
            result += "    " + str(element) + "\n"
        result += ")"
        return result

    def push(self, new):
        """
        Add an element to the top of the stack
        :argument: any type
        :return:
        """
        self.length += 1
        self.body += (new, )

    def pop(self):
        """
        Delete and return the last value of the stack
        :argument: None
        :return: type unknown(depends on the type of the last element of the stack) or None when the stack is empty.
        """
        if self.isEmpty():
            return None
        else:
            last = self.peek()
            self.length -= 1
            self.body = self.body[0:self.length]
            return last

    def peek(self):
        """
        Return the last element on the stack without popping it.
        :argument: None
        :return: type unknown(depends on the type of the last element of the stack) or None when the stack is empty.
        """
        if self.isEmpty():
            return None
        else:
            return self.body[-1]

    def print(self):
        """
        Print the whole stack.
        :argument: None
        :return: None
        """
        print(self)

    def isEmpty(self):
        """
        Check if the stack is empty.
        :argument: None
        :return: Boolean value
        """
        if self.length == 0:
            return True
        else:
            return False


class Sentence:
    def __init__(self):
        self.body = input("Type in one sentence: ")
        temp = self.body.split()
        self.saving_stackly = Stack(())
        for words in temp:
            self.saving_stackly.push(words)

    def inversely_output(self):
        while not self.saving_stackly.isEmpty():
            print(self.saving_stackly.pop(), end = " ")


def main():
    testing = Sentence()
    testing.inversely_output()


if __name__ == '__main__':
    main()
