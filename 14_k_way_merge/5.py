from __future__ import print_function
from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
    minHeap = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if len(minHeap) < k:
                heappush(minHeap, (nums1[i] + nums2[j], i, j))
            else:
                if nums1[i] + nums2[j] < minHeap[0][0]:
                    break
                else:
                    heappop(minHeap)
                    heappush(minHeap, (nums1[i] + nums2[j], i, j))

    result = []
    while minHeap:
        num, i, j = heappop(minHeap)
        result.append([nums1[i], nums2[j]])

    return result


def main():
    print("Pairs with largest sum are: " +
          str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
