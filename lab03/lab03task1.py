import random


class Lab03Task1:

    def demo(self):
        try:
            size = int(input("Enter size of array: "))
            only_positives = []
            positives_and_negatives = []
            for i in range(0, size):
                only_positives.append(random.randint(0, 50))
                positives_and_negatives.append(random.randint(-60, 60))
            print("Beginning arrays:")
            print(*only_positives, sep=',')
            print(*positives_and_negatives, sep=',')
            print("-------------------------------------")
            only_positives = self.insertion_sort(only_positives)
            positives_and_negatives = self.insertion_sort(positives_and_negatives)
            print("After insertion sort:")
            print(*only_positives, sep=',')
            print(*positives_and_negatives, sep=',')
        except ValueError:
            return "Invalid input!"

    def __get_ready_sequence(self, array):
        sequence = [array[0]]
        for index in range(1, len(array)):
            if array[index] > sequence[index - 1]:
                sequence.append(array[index])
            else:
                return sequence

    def __insert_value_sorted(self, value, array):
        if value < array[0]:
            array.insert(0, value)
            return

        if value > array[-1]:
            array.append(value)
            return

        if len(array) == 2:
            array.insert(1, value)
            return

        for index in range(0, len(array)):
            if value <= array[index]:
                array.insert(index, value)
                return

    def insertion_sort(self, array):
        output_array = self.__get_ready_sequence(array)
        while len(output_array) != len(array):
            self.__insert_value_sorted(array[len(output_array)], output_array)
        return output_array


Lab03Task1().demo()
