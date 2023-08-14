import quicksort_excel
from quicksort_excel import quick_sort
from quicksort_excel import data_list

sorted_data = sorted(data_list)
reverse_data = list(reversed(data_list))

def test_unsorted():
    unsorted_list = data_list.copy()
    assert quicksort_excel.quick_sort(unsorted_list) == sorted_data
    
def test_sorted():
    sorted_list = sorted_data.copy()
    assert quicksort_excel.quick_sort(sorted_list) == sorted_data
    
def test_reverse():
    reverse_list = reverse_data.copy()
    assert quicksort_excel.quick_sort(reverse_list) == sorted_data
    
def test_empty():
    empty_list = []
    assert quicksort_excel.quick_sort(empty_list) == []

def test_duplicate():
    duplicate_list = [12, 11, 22, 20, 25, 25, 34, 99]
    assert quicksort_excel.quick_sort(duplicate_list) == [11, 12, 20, 22, 25, 25, 34, 99]

