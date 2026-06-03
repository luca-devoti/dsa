from algorithms import selection_sort_largest, selection_sort_smallest, bubble_sort_default, bubble_sort_optimised, insertion_sort, linear_search, binary_search

def test_selection_sort():
    assert selection_sort_largest([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert selection_sort_smallest([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    assert selection_sort_largest([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert selection_sort_smallest([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    assert selection_sort_largest([1, 3, 5, 2]) == [1, 2, 3, 5]
    assert selection_sort_smallest([1, 3, 5, 2]) == [1, 2, 3, 5]

def test_bubble_sort():
    assert bubble_sort_default([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort_optimised([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    assert bubble_sort_default([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort_optimised([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    assert bubble_sort_default([1, 3, 5, 2]) == [1, 2, 3, 5]
    assert bubble_sort_optimised([1, 3, 5, 2]) == [1, 2, 3, 5]

def test_insertion_sort():
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertion_sort([1, 3, 5, 2]) == [1, 2, 3, 5]

def test_linear_search():
    assert linear_search([5, 10, 0, 105, 35], 5) == 0
    assert linear_search([5, 10, 0, 105, 35], 35) == 4
    assert linear_search([5, 10, 0, 35], 35) == 3
    assert linear_search([5, 10, 0, 105, 35], 100) == -1
    assert linear_search([], 10) == -1 

def test_binary_search():
    assert binary_search([1, 3, 5, 7, 9, 11], 5) == 2
    assert binary_search([1, 3, 5, 7, 9, 11, 13], 7) == 3
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 10) == -1
    assert binary_search([], 5) == -1
