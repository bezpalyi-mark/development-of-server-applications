import uuid


def century_from_year(year):
    return year // 100 + 1


class SimpleElement:
    value = 0
    id = 0

    def __init__(self, value):
        self.value = value
        self.id = uuid.uuid4()

    def __repr__(self):
        return f"Value:{self.value}, ID:{self.id}"

    def __eq__(self, other):
        if isinstance(other, SimpleElement):
            if other.value == self.value:
                return True
            else:
                return False

    def __hash__(self):
        return hash(self.value)

    def bigger_than(self, other):
        if isinstance(other, SimpleElement):
            if other.value < self.value:
                return True
            else:
                return False

    def smaller_then(self, other):
        if isinstance(other, SimpleElement):
            if other.value > self.value:
                return True
            else:
                return False


class Utils:
    # This function takes last element as pivot, places
    # the pivot element at its correct position in sorted
    # array, and places all smaller (smaller than pivot)
    # to left of pivot and all greater elements to right
    # of pivot

    def __partition(self, arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j].smaller_then(pivot) or arr[j].__eq__(pivot):
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index

    # Function to do Quick sort

    def quick_sort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.__partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def find_first_by_value(self, arr, value):
        for el in arr:
            if el.value == value:
                return el

    def __find_min(self, arr):
        return min(list(map(lambda el: el.value, arr)))

    def __find_max(self, arr):
        return max(list(map(lambda el: el.value, arr)))

    def __find(self, finder, arr, size):
        search_value = finder(arr)
        entries = []
        if size > len(arr) - 1:
            size = len(arr) - 1
        for el in arr:
            if len(entries) < size:
                if el.value == search_value:
                    entries.append(el)
            else:
                return entries
        return entries

    def find_with_min_value(self, arr, size):
        return self.__find(self.__find_min, arr, size)

    def find_with_max_value(self, arr, size):
        return self.__find(self.__find_max, arr, size)

    def get_average_value(self, arr):
        return sum(map(lambda el: el.value, arr)) / len(arr)

    def find_all_distinct(self, arr):
        return list(set(arr))


utils = Utils()
arr_test = [SimpleElement(10), SimpleElement(2), SimpleElement(2), SimpleElement(-5), SimpleElement(13),
            SimpleElement(0), SimpleElement(-5), SimpleElement(13), SimpleElement(13)]
n = len(arr_test)
utils.quick_sort(arr_test, 0, n - 1)
print("Sorted array is:")
for element in range(n):
    print("%d" % arr_test[element].value)
print(f"Search element with value 10: {utils.find_first_by_value(arr_test, 10)}")
print(f"Search 1 min element: {utils.find_with_min_value(arr_test, 1)}")
print(f"Search 3 min element: {utils.find_with_min_value(arr_test, 3)}")
print(f"Search 1 max element: {utils.find_with_max_value(arr_test, 1)}")
print(f"Search 3 max element: {utils.find_with_max_value(arr_test, 3)}")
print(f"Average value: {utils.get_average_value(arr_test)}")
print(f"Distinct elements: {utils.find_all_distinct(arr_test)}")
print(f"Century of 2001: {century_from_year(2021)}\n"
      f"Century of 1995: {century_from_year(1995)}\n"
      f"Century of 1234: {century_from_year(1234)}")
