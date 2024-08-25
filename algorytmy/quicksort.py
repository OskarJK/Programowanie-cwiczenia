array = [1,2.2,3.1,45,5,2,33,1,7,9,23,13,4]

def partition(array, start, end):
    pivot = array[end]
    low = start
    high = end - 1

    while True:
        while low <= high and array[low] <= pivot:
            low += 1

        while low <= high and array[high] >= pivot:
            high -= 1


        if low <= high:
            array[low], array[high] = array[high], array[low]

        else:
            break

    array[end], array[low] = array[low], array[end]
    return low

def quickSort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)
        print(array)

quickSort(array, 0, len(array) - 1)
print(array)


