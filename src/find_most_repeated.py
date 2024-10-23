from collections import Counter


def find_most_repeated(elements):
    result = {"elements": [], "repeats": None}

    if not elements:
        return result

    counts_dict = dict(Counter(elements))
    max_count = max(counts_dict.values())

    if max_count == 1:
        return result

    most_repeated = [
        element for element in counts_dict if counts_dict[element] == max_count
    ]

    result["elements"], result["repeats"] = most_repeated, max_count

    return result
