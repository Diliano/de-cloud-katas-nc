from src.roman_numeral_encoder import roman_numeral_encoder


def test_handles_input_that_is_an_exact_match_for_a_roman_numeral():
    # Act
    test_input = 1
    expected = "I"
    # Act
    result = roman_numeral_encoder(test_input)
    # Assert
    assert result == expected

    # Act
    test_input = 10
    expected = "X"
    # Act
    result = roman_numeral_encoder(test_input)
    # Assert
    assert result == expected

    # Act
    test_input = 900
    expected = "CM"
    # Act
    result = roman_numeral_encoder(test_input)
    # Assert
    assert result == expected


def test_builds_roman_numeral_string():
    # Act
    test_input = 2
    expected = "II"
    # Act
    result = roman_numeral_encoder(test_input)
    # Assert
    assert result == expected

    # Act
    test_input = 17
    expected = "XVII"
    # Act
    result = roman_numeral_encoder(test_input)
    # Assert
    assert result == expected

    # Act
    test_input = 60
    expected = "LX"
    # Act
    result = roman_numeral_encoder(test_input)
    # Assert
    assert result == expected

    # Act
    test_input = 75
    expected = "LXXV"
    # Act
    result = roman_numeral_encoder(test_input)
    # Assert
    assert result == expected

    # Act
    test_input = 91
    expected = "XCI"
    # Act
    result = roman_numeral_encoder(test_input)
    # Assert
    assert result == expected
