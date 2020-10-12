def find_subsets(nums):
    subsets = []
    subsets.append([])
    start, end = 0, 0
    for i in range(len(nums)):
        start = 0
        if i > 0 and nums[i] == nums[i - 1]:
            start = end + 1
        end = len(subsets) - 1
        for j in range(start, end + 1):
            tmp = list(subsets[j])
            tmp.append(nums[i])
            subsets.append(tmp)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3, 5])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
