from src.fill_square import fill_square


def test_fills_values_to_form_square_matrix():
    # Arrange
    test_input = [[1, 2, 3], [1, 2], [1]]
    expected = [[1, 2, 3], [1, 2, None], [1, None, None]]
    # Act
    result = fill_square(test_input)
    # Assert
    assert result == expected


def test_fills_rows_to_form_square_matrix():
    # Arrange
    test_input = [[1, 2, 3], [1, 2, 3]]
    expected = [[1, 2, 3], [1, 2, 3], [None, None, None]]
    # Act
    result = fill_square(test_input)
    # Assert
    assert result == expected
