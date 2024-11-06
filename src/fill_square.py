def fill_square(square):
    longest_row = max([len(row) for row in square])
    num_rows = len(square)

    dimension = longest_row if longest_row > num_rows else num_rows

    result = []

    # build result using existing rows, checking for missing values
    for row in square:
        difference = dimension - len(row)
        row.extend([None for _ in range(difference)])
        result.append(row)

    # build missing rows if required
    difference = dimension - len(result)
    for _ in range(difference):
        result.append([None for _ in range(dimension)])

    return result
