class SimpleElement:
    value = 0

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, SimpleElement):
            if other.value == self.value:
                return True
            else:
                return False

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

    def partition(self, arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
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
            pi = self.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def index_of(self, arr, element):
        if isinstance(arr, list):
            arr.index(element)


# Driver code to test above
utils = Utils()
arr_test = [SimpleElement(10), SimpleElement(2), SimpleElement(-5), SimpleElement(13), SimpleElement(0)]
n = len(arr_test)
utils.quick_sort(arr_test, 0, n - 1)
print("Sorted array is:")
for element in range(n):
    print("%d" % arr_test[element])
