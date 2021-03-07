
from merge_sort.merge_sort import merge_sort



def test_unsorted_list():
    expected = [4, 8, 15, 16, 23, 42]
    actual = merge_sort([8, 4, 23, 42, 16, 15])
    assert actual == expected

def test_unsorted_list_with_negatives():
    expected = [-16, -4, 8, 15, 23, 42]
    actual = merge_sort([8, -4, 23, 42, -16, 15])
    assert actual == expected

def test_short_list():
    expected = "2 or more numbers needed to sort"
    actual = merge_sort([8])
    assert actual == expected