from SimpleElement import SimpleElement
from Utils import Utils
from Utils import century_from_year

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
      f"Century of 1234: {century_from_year(1234)}\n"
      f"Century with default parameter: {century_from_year()}")
