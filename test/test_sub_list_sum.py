from src.sub_list_sum import sub_list_sum

"""
The test suite accompanies the solution, however this was not built with 
a full TDD approach (only for the first three tests).

I researched the textual / plain English description of Kadane's Algorithm 
and used this to write out a walkthrough of the input example 
[-2, 1, -3, 4, -1, 2, 1, -5, 4]. I then converted this write out into the 
remainder of the code solution.
"""


def test_default_behaviour_returns_0_given_only_negative_numbers():
    # Arrange
    test_input = [-1, -2, -3, -4, -5]
    expected = 0
    # Act
    result = sub_list_sum(test_input)
    # Assert
    assert result == expected


def test_default_behaviour_returns_0_given_empty_list():
    # Arrange
    test_input = []
    expected = 0
    # Act
    result = sub_list_sum(test_input)
    # Assert
    assert result == expected


def test_calculates_sum_of_list_given_only_positive_numbers():
    # Arrange
    test_input = [1, 2, 3, 4, 5]
    expected = 15
    # Act
    result = sub_list_sum(test_input)
    # Assert
    assert result == expected


def test_calculates_maximum_sub_list_sum():
    # Arrange
    test_input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    # Act
    result = sub_list_sum(test_input)
    # Assert
    assert result == expected

    # Arrange
    test_input = [9, 8, 7, -3, 6, 5, 4, -3, 2, 1]
    expected = 36
    # Act
    result = sub_list_sum(test_input)
    # Assert
    assert result == expected

    # Arrange
    test_input = [5, -6, 2, 9, -4, -3, 8, -10, 20]
    expected = 22
    # Act
    result = sub_list_sum(test_input)
    # Assert
    assert result == expected
