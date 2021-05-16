import re

FILES_NAMES = tuple(["resources/input.txt", "resources/even_output.txt",
                     "resources/odd_output.txt", "resources/a_o_replaced_file.txt"])


class FileHandler:

    def replace_a_by_o_and_vice_versa(self, line):
        a_indexes = [m.start() for m in re.finditer('a', line)]
        o_indexes = [m.start() for m in re.finditer('o', line)]
        str_list = list(line)
        for index in a_indexes:
            str_list[index] = 'o'
        for index in o_indexes:
            str_list[index] = 'a'
        return "".join(str_list)

    def read_file_and_write_outputs(self):
        try:
            with open(FILES_NAMES[0], 'r') as input_file, open(FILES_NAMES[1], 'w') as even_output_file, \
                    open(FILES_NAMES[2], 'w') as odd_output_file, open(FILES_NAMES[3], 'w') as a_o_replaced_file:
                index = 1
                for line in input_file:
                    if index % 2 == 0:
                        even_output_file.write(line)
                    else:
                        odd_output_file.write(line)
                    index += 1
                    a_o_replaced_file.write(self.replace_a_by_o_and_vice_versa(line))
        except FileNotFoundError:
            print("No such file: " + FILES_NAMES[0])


FileHandler().read_file_and_write_outputs()
