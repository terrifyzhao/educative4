def remove_element(arr, key):
    next, i = 0, 0
    while i < len(arr):
        if arr[i] != key:
            arr[next] = key
            next += 1
        i += 1
    return next


def main():
    print("Array new length: " +
          str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " +
          str(remove_element([2, 11, 2, 2, 1], 2)))


main()
