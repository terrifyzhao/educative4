from heapq import *


def rearrange_string(str):
    dic = {}
    res = []
    max_heap = []
    for num in str:
        dic[num] = dic.get(num, 0) + 1

    for k, v in dic.items():
        heappush(max_heap, (-v, k))

    pre_char = ''
    pre_fre = 0
    while max_heap:
        fre, char = heappop(max_heap)
        if pre_char and -pre_fre > 0:
            heappush(max_heap, (pre_fre, pre_char))

        res.append(char)
        pre_char = char
        pre_fre = fre+1

    return "".join(res) if len(res) == len(str) else ''


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
