from collections import deque


def find_permutations(nums):
    result = []
    permutations = deque()
    permutations.append([])
    for i in range(len(nums)):
        size = len(permutations)
        for _ in range(size):
            old_permutation = permutations.popleft()
            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, nums[i])
                if len(new_permutation) == len(nums):
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)

    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
