import math


class Lab0102:
    cache = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

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

    def __next_prime(self, prev_prime):
        if prev_prime <= 1:
            return self.cache[0]
        elif prev_prime <= self.cache[len(self.cache) - 1]:
            for prime in self.cache:
                if prime > prev_prime:
                    return prime
        else:
            new_prime = prev_prime
            while not self.__is_prime(new_prime):
                new_prime += 1
            self.cache.append(prev_prime)
            return new_prime

    def __get_prime_dividers(self, number):
        prime_dividers = []
        prime = self.__next_prime(0)
        while not number == 1:
            if number % prime == 0:
                prime_dividers.append(prime)
                number /= prime
                prime = self.__next_prime(0)
            else:
                prime = self.__next_prime(prime)
        return prime_dividers

    def __symmetric_intersection(self, arr1, arr2):
        result = 1
        for prime in arr1:
            if prime in arr2:
                result *= prime
                arr2.remove(prime)
        return result

    def calculate_equation(self):
        user_input = input("Enter angle value: ")
        try:
            angle = float(user_input)
            return math.cos(angle) + math.cos(2 * angle) + math.cos(6 * angle) + math.cos(7 * angle)
        except ValueError:
            return "Error: " + user_input + " is not a number"

    def greatest_common_divisor_and_least_common_multiple(self):
        x_input = input("Enter x value: ")
        y_input = input("Enter y value: ")
        try:
            x_input = float(x_input)
            y_input = float(y_input)
            result = y_input / x_input if x_input > y_input else x_input / y_input
            if result.is_integer():
                return result
            else:
                x_prime_dividers = self.__get_prime_dividers(x_input)
                y_prime_dividers = self.__get_prime_dividers(y_input)
                gtd = self.__symmetric_intersection(x_prime_dividers, y_prime_dividers)
                return {
                    "GTD": gtd,
                    "LCM": int((x_input * y_input) / gtd)
                }
        except ValueError:
            return "Error: Input must be numeric"


program = Lab0102()
print("The equation: cos(a) + cos(2a) + cos(6a) + cos(7a)")
print(program.calculate_equation())
print("The greatest common divisor and the least common multiple of x and y")
gtd_and_lcm = program.greatest_common_divisor_and_least_common_multiple()
print(f"The greatest common divisor is: {gtd_and_lcm.get('GTD')}")
print(f"The least common multiple is: {gtd_and_lcm.get('LCM')}")
