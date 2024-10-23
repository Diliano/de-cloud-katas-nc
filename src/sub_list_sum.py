def sub_list_sum(sequence):
    # also handles empty list as all() will default to True
    if all(num < 0 for num in sequence):
        return 0

    if all(num > 0 for num in sequence):
        return sum(sequence)

    max_sum = sequence[0]
    running_sum = sequence[0]

    for num in sequence[1:]:
        if (running_sum + num) > num:
            running_sum += num
        else:
            running_sum = num

        if running_sum > max_sum:
            max_sum = running_sum

    return max_sum
