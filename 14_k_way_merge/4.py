from heapq import *


def find_smallest_range(lists):
    min_heap = []

    max_num = 0
    for list in lists:
        max_num = max(max_num, list[0])
        heappush(min_heap, (list[0], 0, list))

    start = 0
    end = 1000

    while len(min_heap) == len(lists):
        value, index, list = heappop(min_heap)
        if end - start > max_num - value:
            start = value
            end = max_num

        index += 1
        if index < len(list):
            heappush(min_heap, (list[index], index, list))
            max_num = max(max_num, list[index])

    return [start, end]


def main():
    print("Smallest range is: " +
          str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
