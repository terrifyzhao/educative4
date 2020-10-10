def remove_duplicates(arr):
    next, i = 1, 1
    while i < len(arr):
        if arr[next - 1] != arr[i]:
            arr[next] = arr[i]
            next += 1
        i += 1
    return next


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
