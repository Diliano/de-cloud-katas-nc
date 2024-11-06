def fill_square(square):
    longest_row = max([len(row) for row in square])
    num_rows = len(square)
    dimension = None

    if longest_row > num_rows:
        dimension = longest_row
    else:
        dimension = num_rows

    result = []

    for row in square:
        if len(row) == dimension:
            result.append(row)
        else:
            difference = dimension - len(row)
            row.extend([None for _ in range(difference)])
            result.append(row)

    if len(result) < dimension:
        difference = dimension - len(result)
        for _ in range(difference):
            result.append([None for _ in range(dimension)])

    return result
