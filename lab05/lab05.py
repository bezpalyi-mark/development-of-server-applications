from collections import Counter
import random

__sentence = 'I have a wonderful dream'


class Lab05:
    __array_a = list('abcd')

    __array_b = list('dfge')

    def __is_prime(self, number):
        if number <= 1:
            return False
        elif number == 2 or number == 3:
            return True
        else:
            for i in range(2, number):
                if number % i == 0:
                    return False
            return True

    def get_single_characters_in_sentence(self, sentence):
        return set({char: count for char, count in dict(Counter(sentence)).items() if count == 1}.keys())

    def add_to_b_array(self, char):
        if char not in self.__array_a:
            self.__array_b.append(char)
        else:
            self.__array_b.remove(char)

    def print_arrays(self):
        print(f"a:{self.__array_a}")
        print(f"b:{self.__array_b}")

    def get_x_y_z_arrays_from(self, source_array):
        return {
            "x": list(filter(lambda number: isinstance(number, int), source_array)),
            "y": list(filter(lambda number: isinstance(number, int) and self.__is_prime(number), source_array)),
            "z": list(filter(lambda number: isinstance(number, int) and not self.__is_prime(number), source_array))
        }


program = Lab05()
print(f"Single characters in sentence '{__sentence}':\n {program.get_single_characters_in_sentence(__sentence)}")
program.print_arrays()
print("Add 'd' character")
program.add_to_b_array('d')
program.print_arrays()
print("Add 'h' character")
program.add_to_b_array('h')
program.print_arrays()

random_data = list()
for index in range(0, 20):
    random_data.append(random.randint(8, 102))
print(f"Random data:{random_data}")
print(f"Filtered lists: {program.get_x_y_z_arrays_from(random_data)}")
