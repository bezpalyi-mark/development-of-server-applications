import random


class Lab03Task2:
    def __is_special(self, row, column, array2d):
        special = True
        element = array2d[row][column]
        if not (column == 0 or column == (len(array2d) - 1)):  # checks that number not in the end or beginning of row
            for index in range(0, len(array2d[row])):
                if index < column and element < array2d[row][index]:
                    special = False
                elif index > column and element > array2d[row][index]:
                    special = False
            if special:
                return True
        total = 0
        for index in range(0, len(array2d)):
            if not index == row:
                if not column >= len(array2d[index]):  # check if the row have not enough columns
                    total += array2d[index][column]
        return True if total < element else False

    def count_specials(self, array2d):
        counter = 0
        for row_index in range(0, len(array2d)):
            for column_index in range(0, len(array2d[row_index])):
                if self.__is_special(row_index, column_index, array2d):
                    counter += 1
        return counter


def demo():
    program = Lab03Task2()
    try:
        row_size = int(input("Enter rows amount: "))
        column_size = int(input("Enter columns amount: "))
        array2d = []
        for row_index in range(0, row_size):
            array = []
            for column_index in range(0, column_size):
                array.append(random.randint(-10, 10))
            array2d.append(array)
        amount = program.count_specials(array2d)
        print(f"Specials total: {amount}")
    except ValueError:
        return "Invalid input!"


demo()
