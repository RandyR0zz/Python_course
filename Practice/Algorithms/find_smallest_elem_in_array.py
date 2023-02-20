def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def select(arr):
    list = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        list.append(arr.pop(smallest))
    return list