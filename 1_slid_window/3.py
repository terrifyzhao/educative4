def longest_substring_with_k_distinct(str1, k):
    start = 0
    max_len = 0

    dic = {}
    for i in range(len(str1)):
        s = str1[i]
        dic[s] = dic.get(s, 0) + 1

        while len(dic) > k:
            s = str1[start]

            dic[s] -= 1
            if dic[s] == 0:
                del dic[s]
            start += 1
        max_len = max(max_len, i - start + 1)
    return max_len


def main():
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
