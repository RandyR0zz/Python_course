def binary_search(array, n):
    list = sorted(array)
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)//2
        target = list[mid]
        if target == n:
            return mid
        elif target > n:
            high = mid - 1
        else:
            low = mid + 1
    return -1