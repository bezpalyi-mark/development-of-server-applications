from time import sleep
from random import randint
from decorators import *


@tracker_decorator
def very_complicated_function(argument):
    print(f"You gave me {argument}")
    print("Processing something...")
    sleep(3)


@decorator_factory(max_attempts=20)
def potential_broken_function():
    value = randint(0, 5)
    if value != 5:
        print(f"Not this time...")
        return False
    print("Got it!")
    return True


def collect_all_decorated_functions():
    if hasattr(very_complicated_function, "wrapped"):
        REGISTERED.append(very_complicated_function.__name__)
    if hasattr(potential_broken_function, "wrapped"):
        REGISTERED.append(potential_broken_function.__name__)


very_complicated_function()
potential_broken_function()
decorated_not_by_annotation = collect_decorator(collect_all_decorated_functions)
decorated_not_by_annotation()
