def find_letter_case_string_permutations(str):
    permutations = []

    permutations.append(str)

    for i in range(len(str)):
        if str[i].isalpha():
            size = len(permutations)
            for j in range(size):
                permutation = list(permutations[j])
                permutation[i] = permutation[i].swapcase()
                permutations.append(''.join(permutation))

    return permutations


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
