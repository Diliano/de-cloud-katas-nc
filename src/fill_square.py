def fill_square(square):
    longest_row = max([len(row) for row in square])

    result = []

    for row in square:
        if len(row) == longest_row:
            result.append(row)
        else:
            while len(row) != longest_row:
                row.append(None)
            result.append(row)

    return result
