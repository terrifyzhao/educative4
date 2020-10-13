from heapq import *


def find_Kth_smallest(lists, k):
    number = -1

    min_heap = []

    for list in lists:
        heappush(min_heap, (list[0], 0, list))

    while k:
        value, index, list = heappop(min_heap)
        index += 1
        if index < len(list):
            heappush(min_heap, (list[index], index, list))
        k -= 1

    return value


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
