from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    result = []

    for i in range(len(ropeLengths)):
        heappush(result, ropeLengths[i])

    res = 0
    while len(result) > 1:
        r1 = heappop(result)
        r2 = heappop(result)
        res += r1 + r2
        heappush(result, r1 + r2)

    return res


def main():
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
