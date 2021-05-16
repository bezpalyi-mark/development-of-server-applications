from datetime import datetime

REGISTERED = []


def tracker_decorator(func):
    def wrap():
        begin = datetime.now()
        func("an apple")
        end = datetime.now()
        print(f"The function 1 was completed in {end - begin}")

        # Carrying metadata
        wrap.__doc__ = func.__doc__
        wrap.__name__ = func.__name__
        wrap.__setattr__("wrapped", True)

    return wrap


def decorator_factory(max_attempts):
    def restart_if_fault(func):
        def wrap():
            success = False
            iter_number = 0
            while not success and max_attempts != iter_number:
                iter_number += 1
                success = func()
            print(f"The function 2 completed successfully on the {iter_number} attempt")

            # Carrying metadata
            wrap.__doc__ = func.__doc__
            wrap.__name__ = func.__name__
            wrap.__setattr__("wrapped", True)

        return wrap

    return restart_if_fault


def collect_decorator(func):
    def wrap():
        print("Collecting all decorated functions...")
        func()
        print(f"Decorated functions: {REGISTERED}")

    return wrap
