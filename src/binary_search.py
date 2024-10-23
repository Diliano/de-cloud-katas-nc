def binary_search(lst, target, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(lst) - 1

    if left > right:
        return -1

    middle = (left + right) // 2

    if lst[middle] == target:
        return middle

    if lst[middle] < target:
        return binary_search(lst, target, left=middle + 1, right=right)
    else:
        return binary_search(lst, target, left=left, right=middle - 1)
