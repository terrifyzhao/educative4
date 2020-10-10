import math


def shortest_window_sort(arr):
    low, high = 0, len(arr) - 1

    while low < len(arr) - 1:
        if arr[low + 1] < arr[low]:
            break
        low += 1

    if low == len(arr) - 1:
        return 0

    while high > 0:
        if arr[high - 1] > arr[high]:
            break
        high -= 1

    min_num = min(arr[low:high + 1])
    max_num = max(arr[low:high + 1])

    while low > 0 and arr[low - 1] > min_num:
        low -= 1
    while high < len(arr) - 1 and arr[high + 1] < max_num:
        high += 1

    return high - low + 1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))


main()
