def quick_sort(arr, start, end):
    left, right = start, end

    if left < right:
        pivot = arr[left]
        while left != right:
            while left < right and arr[right] > pivot:
                right -= 1
            arr[left] = arr[right]

            while left < right and arr[left] < pivot:
                left += 1
            arr[right] = arr[left]

        arr[left] = pivot
        quick_sort(arr, start, left - 1)
        quick_sort(arr, right + 1, end)


arr = [2, 1, 3, 54, 10, 13]
quick_sort(arr, 0, 5)
print(arr)
