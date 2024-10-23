from src.binary_search import binary_search


def test_determines_index_of_target():
    # Arrange
    test_input = [1, 2, 5, 9, 12, 19, 27]
    test_target = 12
    expected = 4
    # Act
    result = binary_search(test_input, test_target)
    # Assert
    assert result == expected

    # Arrange
    test_input = [1, 2, 5, 9, 12, 19, 27]
    test_target = 9
    expected = 3
    # Act
    result = binary_search(test_input, test_target)
    # Assert
    assert result == expected

    # Arrange
    test_input = [1, 2, 5, 9]
    test_target = 5
    expected = 2
    # Act
    result = binary_search(test_input, test_target)
    # Assert
    assert result == expected


def test_default_behaviour_returns_minus_one_if_target_not_present_in_list():
    # Arrange
    test_input = [1, 2, 5, 9]
    test_target = 15
    expected = -1
    # Act
    result = binary_search(test_input, test_target)
    # Assert
    assert result == expected
