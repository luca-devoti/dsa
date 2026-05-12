from algorithms import selection_sort_largest, selection_sort_smallest

def test_selection_sort():
    assert selection_sort_largest([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert selection_sort_smallest([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    assert selection_sort_largest([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert selection_sort_smallest([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    assert selection_sort_largest([1, 3, 5, 2, 4]) == [1, 2, 3, 4, 5]
    assert selection_sort_smallest([1, 3, 5, 2, 4]) == [1, 2, 3, 4, 5]