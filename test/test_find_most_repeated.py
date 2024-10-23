from src.find_most_repeated import find_most_repeated


def test_default_behaviour_given_empty_list():
    # Arrange
    test_input = []
    expected = {"elements": [], "repeats": None}
    # Act
    result = find_most_repeated(test_input)
    # Assert
    assert result == expected


def test_default_behaviour_given_list_with_no_repeated_elements():
    # Arrange
    test_input = ["foo", "bar", "hello", "world"]
    expected = {"elements": [], "repeats": None}
    # Act
    result = find_most_repeated(test_input)
    # Assert
    assert result == expected


def test_calculates_most_repeated_element_in_given_list():
    # Arrange
    test_input = ["foo", "foo", "bar", "hello", "world"]
    expected = {"elements": ["foo"], "repeats": 2}
    # Act
    result = find_most_repeated(test_input)
    # Assert
    assert result == expected


def test_calculates_most_repeated_elements_in_given_list():
    # Arrange
    test_input = ["foo", "foo", 1, 2, 3, "bar", 2, 3, 4, "bar", "bar", "foo"]
    expected = {"elements": ["foo", "bar"], "repeats": 3}
    # Act
    result = find_most_repeated(test_input)
    # Assert
    assert result == expected
