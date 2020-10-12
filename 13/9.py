from heapq import *


def find_maximum_distinct_elements(nums, K):
    min_heap = []

    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    for k, v in dic.items():
        heappush(min_heap, (v, k))

    count = 0
    while min_heap:
        v, k = heappop(min_heap)
        if v == 1:
            count += 1
        else:
            K = K - v + 1
            if K >= 0:
                count += 1
    if K > 0:
        count -= K

    return count


def main():
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
