import random

__passengers = ["Mike", "John", "Doctor Who", "Miki", "Kate", "Oliver", "Viktor", "Amelia", "Rose", "Aaron"]


class Baggage:
    weight = 0
    stuff_count = 0

    def __init__(self, weight, stuff_count):
        self.weight = weight
        self.stuff_count = stuff_count

    def __repr__(self):
        return f"[Weight: {self.weight}; Stuff Count: {self.stuff_count}]"


class Lab04:
    def get_with_more_than_two_things(self, pass_bag_dict):
        return {passenger: bag for passenger, bag in pass_bag_dict.items() if bag.stuff_count > 2}

    def is_exists_with_one_thing_weight_less_25_kg(self, pass_bag_dict):
        return len(
            {passenger: bag for passenger, bag in pass_bag_dict.items() if
             bag.stuff_count == 2 and bag.weight < 25}) >= 1

    def get_with_extra_baggage(self, pass_bag_dict):
        average = sum(map(lambda value: value.stuff_count, pass_bag_dict.values())) / len(pass_bag_dict)
        return len({passenger: bag for passenger, bag in pass_bag_dict.items() if bag.stuff_count > average})

    def get_common_baggage_number(self, pass_bag_dict):
        average_weight = sum(map(lambda value: value.weight, pass_bag_dict.values())) / len(pass_bag_dict)
        return len({passenger: bag for passenger, bag in pass_bag_dict.items() if (bag.weight - average_weight) <= 0.5})


def demo():
    pass_bag = {}
    for passenger in __passengers:
        pass_bag[passenger] = Baggage(random.randint(0, 10), random.randint(0, 30))
    program = Lab04()
    print(f"Passengers with more than two things: {program.get_with_more_than_two_things(pass_bag)}")
    print(f"Is there a passenger with baggage containing only one item weighing less than 25 kg: "
          f"{program.is_exists_with_one_thing_weight_less_25_kg(pass_bag)}")
    print(f"Number of passengers with more than average items in their baggage: "
          f"{program.get_with_extra_baggage(pass_bag)}")
    print(f"Number of common baggage {program.get_common_baggage_number(pass_bag)}")


demo()
