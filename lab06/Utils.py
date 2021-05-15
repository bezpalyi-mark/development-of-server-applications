from datetime import date


def century_from_year(year=date.today().year):
    return year // 100 + 1


class Utils:
    """
     This function takes last element as pivot, places
     the pivot element at its correct position in sorted
     array, and places all smaller (smaller than pivot)
     to left of pivot and all greater elements to right
     of pivot
    """

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

    """
     The main function that implements QuickSort
     arr[] --> Array to be sorted,
     low  --> Starting index,
     high  --> Ending index
     Function to do Quick sort
    """

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

    """
     Function to find first element that contains searching value
    """

    def find_first_by_value(self, arr, value):
        for el in arr:
            if el.value == value:
                return el

    """
     Function to find min value in list of SimpleElement classes
    """

    def __find_min(self, arr):
        return min(list(map(lambda el: el.value, arr)))

    """
     Function to find max value in list of SimpleElement classes
    """

    def __find_max(self, arr):
        return max(list(map(lambda el: el.value, arr)))

    """
     The main logic of searching elements with defined value limited by size 
    """

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

    """
     The public function of searching MIN elements limited by size 
    """

    def find_with_min_value(self, arr, size):
        return self.__find(self.__find_min, arr, size)

    """
     The public function of searching MAX elements limited by size 
    """

    def find_with_max_value(self, arr, size):
        return self.__find(self.__find_max, arr, size)

    """
     Function to find average value in list of SimpleElement classes
    """

    def get_average_value(self, arr):
        return sum(map(lambda el: el.value, arr)) / len(arr)

    """
     Function to find unique elements in list of SimpleElement classes
    """

    def find_all_distinct(self, arr):
        return list(set(arr))
