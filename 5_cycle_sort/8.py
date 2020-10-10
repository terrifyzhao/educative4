def find_first_k_missing_positive(nums, k):
    n = len(nums)
    i = 0
    while i < len(nums):
        index = nums[i] - 1
        if 0 <= index < len(nums) and nums[i] != nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
        else:
            i += 1
    res = []
    max_num = 0
    other_num = set()
    for i in range(len(nums)):
        if nums[i] != i + 1 and len(res) < k:
            res.append(i + 1)
            other_num.add(nums[i])

    i = 1
    while len(res) < k:
        num = n + i
        if num not in other_num:
            res.append(n + i)
        i += 1
    return res


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()
