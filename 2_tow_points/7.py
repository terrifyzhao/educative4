from collections import deque


def find_subarrays(arr, target):
    result = []
    product = 1
    start = 0

    for i in range(len(arr)):
        num = arr[i]
        product *= num
        if product >= target:
            product /= arr[start]
            start += 1

        queue = deque()
        for j in range(i, start - 1, -1):
            queue.append(arr[j])
            result.append(list(queue))
    return result


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()
