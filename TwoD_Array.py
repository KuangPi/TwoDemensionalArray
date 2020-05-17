import sys
"""

Copyright 2020 Qiaoyu Zhang

Version of python: Python 3.7

"""

"""
This module provides a object type called 2d array which could be described as the list of list of two object. 
2d array has 7 methods: insert, print, remove, append, change, pop, high
To be noticed that even though 2d array is called as an array, it still receives all kinds of different object type 
unlike the real array in numpy. 
"""


class TwoD_Array_List:
    """
    Holds and creates the array in the form of a table using list of lists
    The values can only be integers.

    :Attributes: *values(integer), number of row, number of column
    """
    def __init__(self, number_of_row, number_of_column, *values):
        values_list = list(values)
        self.rowLength = number_of_row
        self.columnLength = number_of_column
        self.body = []
        for i in range(self.rowLength):
            self.body.append([])
            for j in range(self.columnLength):
                self.body[i].append(values_list[i * self.columnLength + j])

    def __str__(self):
        results = "[\n"
        for elements in self.body:
            results += "    " + str(elements) + "\n"
        results += "]"
        return results

    def change(self, value, Xposition, Yposition):
        """
        Change the value to given value at given position (x, y)

        :parameter: value, Xposition, Yposition:
        :return: None
        """
        assert Xposition <= self.columnLength and Yposition <= self.columnLength
        self.body[Yposition][Xposition] = value

    def printall(self):
        """
        Print the 2d array

        :return None
        """
        print(self)

    def printsingle(self, Xposition, Yposition):
        """
        This method print the value at the given palce.

        :parameter Xposition,Yposition
        :return: None
        """
        print(self.body[Yposition][Xposition])

    def remove(self, identifier, position):
        """
        Remove a column or a row.
        :parameter: identifier(True for column, False for row), position
        :return: None
        """
        if identifier:
            for i in range(self.rowLength):
                self.body[i].pop(position)
            self.columnLength -= 1
        else:
            self.body.pop(position)
            self.rowLength -= 1

    def append(self, identifier, values):
        """
        Append a column or a row at the end of the 2d array.
        :parameter: identifier(True for column, False for row), values(tuple please)
        :return: None
        """
        values_list = list(values)
        if identifier:
            assert len(values) == self.rowLength
            for i in range(self.rowLength):
                self.body[i].append(values_list[i])
            self.columnLength += 1
        else:
            assert len(values) == self.columnLength
            self.body.append(values_list)
            self.rowLength += 1

    def insert(self, identifier, values, position):
        """
        This function could insert a row or a column to the place you want.

        :parameter: identifier(True for column, False for row), values(tuple please), position
        :return: None
        """
        values_list = list(values)
        if identifier:
            assert len(values) == self.rowLength
            for i in range(self.rowLength):
                self.body[i].insert(position, values_list[i])
                self.columnLength += 1
        else:
            assert len(values) == self.columnLength
            self.body.insert(position, values_list)
            self.rowLength += 1

    def high(self, identifier):
        """
        This function will find the highest combination of the sum either vertically or horizontally.
        :parameter: identifier(True for column, False for row)
        :return: The highest pair as tuple.
        """
        if identifier:
            sum_dict = dict()
            if sum_dict != {}:
                sum_dict.clear()
            for i in range(self.rowLength):
                temp_sum = 0
                temp_used = []
                for j in range(self.columnLength):
                    temp_sum += self.body[j][i]
                    temp_used.append(self.body[j][i])
                if temp_sum not in sum_dict:
                    sum_dict[temp_sum] = [tuple(temp_used)]
                else:
                    sum_dict[temp_sum] += (tuple(temp_used))
            temp_high = 0
            for key in sum_dict:
                temp_high = 0
                if key > temp_high:
                    temp_high = key
                elif key == temp_high:
                    raise UserWarning()
            return sum_dict[temp_high][0]
        else:
            sum_dict = dict()
            if sum_dict != {}:
                sum_dict.clear()
            for rows in self.body:
                add_result = 0
                for elements in rows:
                    add_result += elements
                if add_result not in sum_dict:
                    sum_dict[add_result] = [tuple(rows)]
                else:
                    sum_dict[add_result] += (tuple(rows))
            temp_high = 0
            for key in sum_dict:
                temp_high = 0
                if key > temp_high:
                    temp_high = key
                elif key == temp_high:
                    raise UserWarning()
            return sum_dict[temp_high][0]

    def pop(self):
        """
        :return: The last element of the array.
        """
        temp = self.body[self.columnLength - 1][self.rowLength - 1]
        self.body[self.columnLength - 1][self.rowLength - 1] = 0
        return temp


def execution(TwoDArray):
    order = input(">>>")
    if order == "printall":
        TwoDArray.printall()
        print("When using the module, you should enter the following to get the same effect: ")
        print("'Name of the array'.printall()")
    elif order == "printsingle":
        print("Please enter the position: ")
        x = int(input("X: "))
        y = int(input("Y: "))
        print("Here is the result: ")
        TwoDArray.printsingle(x, y)
        print("When using the module, you should enter the following to get the same effect: ")
        print("'Name of the Array'.printsingle(%d, %d)" % (x, y))
    elif order == "change":
        print("Please enter the X and Y position of the value you want to change")
        x = int(input("x: "))
        y = int(input("y: "))
        print("It currently is:", end=" ")
        TwoDArray.printsingle(x, y)
        value = int(input("What value do you want to change it into? "))
        TwoDArray.change(value, x, y)
        print("Changing finished")
        print("This is the result after changing:")
        TwoDArray.printall()
        print("When using the module, you should enter the following to get the same effect: ")
        print("'Name of the array'.change(%d, %d, %d)" % (value, x, y))
    elif order == "remove":
        print("Please enter if you want to remove a row or a column: ")
        if input("Enter 'row' or 'column': ") == "row":
            row = int(input("Please enter which column needs to be delete: "))
            TwoDArray.remove(False, row)
            print("This is the result: ")
            TwoDArray.printall()
            print("When using the module, you should enter the following to get the same effect: ")
            print("'Name of the array'.remove(False, %d)" % row)
        else:
            column = int(input("Please enter which column needs to be delete: "))
            TwoDArray.remove(True, column)
            print("This is the result: ")
            TwoDArray.printall()
            print("When using the module, you should enter the following to get the same effect: ")
            print("'Name of the array'.remove(True, %d)" % column)
    elif order == "pop":
        print("This is the return value: ")
        print(TwoDArray.pop())
        print("This is the array after change: ")
        TwoDArray.printall()
        print("When using the module, you should enter the following to get the same effect: ")
        print("'Name of the array'.pop()")
    elif order == "high":
        print("Please enter if you want to compare by row or column: ")
        if input("Enter 'row' or 'column': ") == "row":
            print(TwoDArray.high(False))
            print("When using the module, you should enter the following to get the same effect: ")
            print("'Name of the array'.high(False)")
        else:
                print(TwoDArray.high(True))
                print("When using the module, you should enter the following to get the same effect: ")
                print("'Name of the array'.high(True)")
    elif order == "append":
        print("Please enter if you want to append a row or a column: ")
        if input("Enter 'row' or 'column': ") == "row":
            print("Please enter the values. Needs %d in total. One line each: " % TwoDArray.columnLength)
            values = ()
            for i in range(TwoDArray.columnLength):
                values += (int(input()),)
            TwoDArray.append(False, values)
            print("This is the result: ")
            TwoDArray.printall()
            print("When using the module, you should enter the following to get the same effect: ")
            print("'Name of the array'.append(False, ", values)
        else:
            print("Please enter the values. Needs %d in total. One line each: " % TwoDArray.rowLength)
            values = ()
            for i in range(TwoDArray.rowLength):
                values += (int(input()),)
            TwoDArray.append(True, values)
            print("This is the result: ")
            TwoDArray.printall()
            print("When using the module, you should enter the following to get the same effect: ")
            print("'Name of the array'.append(True, ", values)
    elif order == "insert":
        print("Please enter if you want to insert a row or a column: ")
        if input("Enter 'row' or 'column': ") == "row":
            position = int(input("Please enter the position you want it to be inserted in: "))
            print("Please enter the values. Needs %d in total. One line each: " % TwoDArray.columnLength)
            values = ()
            for i in range(TwoDArray.columnLength):
                values += (int(input()),)
            TwoDArray.insert(False, values, position)
            print("This is the result: ")
            TwoDArray.printall()
            print("When using the module, you should enter the following to get the same effect: ")
            print("'Name of the array'.insert(False, ", values, ",", position, ")")
        else:
            position = int(input("Please enter the position you want it to be inserted in: "))
            print("Please enter the values. Needs %d in total. One line each: " % TwoDArray.rowLength)
            values = ()
            for i in range(TwoDArray.rowLength):
                values += (int(input()),)
            TwoDArray.insert(True, values, position)
            print("This is the result: ")
            TwoDArray.printall()
            print("When using the module, you should enter the following to get the same effect: ")
            print("'Name of the array'.insert(True, ", values, ",", position, ")")
    elif order == "help":
        print("The following are commands that executable: ")
        print("""change
        printall
        printsingle
        remove
        append
        high
        pop
        """)
    elif order == "finished":
        print("Thanks for using. Quiting now...")
        sys.exit(0)
    else:
        print("Cannot recognize the order, please check and type again. ")
        print("type 'help' to get all the supported statements. ")
    execution(TwoDArray)


def main():
    """
    This function provides an UI for trying the module

    Doesn't require any arguments

    return: None
    """
    print("Type codes here in order to try the module. ")
    print("Some of the codes is not done as the brief description asked. ")
    print("Remove and append are changed in a more reasonable way. ")
    print("To make your life easier, a 2d array is already prepared here:")
    test = TwoD_Array_List(3, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    test.printall()
    execution(test)


if __name__ == '__main__':
    main()
