def find_all_duplicates(nums):
    i = 0
    duplicateNumbers = []

    while i < len(nums):
        index = nums[i]-1
        if index < len(nums) and nums[i] != nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicateNumbers.append(nums[i])

    return duplicateNumbers


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()
