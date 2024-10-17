from array import array

from multiprocessingAULA import results


def binary_search(ar, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if ar[mid] == x:
            return mid
        elif ar[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 4

result = binary_search(arr, x, 0, len(arr)-1)

if result != -1:
    print('element is present at index ' + str(result))