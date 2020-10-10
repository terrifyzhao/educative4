def find_string_anagrams(str1, pattern):
    start = 0
    res = []
    match = 0
    dic = {}
    for s in pattern:
        dic[s] = dic.get(s, 0) + 1

    for i in range(len(str1)):
        s = str1[i]
        if s in dic:
            dic[s] -= 1
            if dic[s] == 0:
                match += 1

        if match == len(dic):
            res.append(start)

        if i >= len(pattern)-1:
            s = str1[start]
            start += 1

            if s in dic:
                if dic[s] == 0:
                    match -= 1
                dic[s] += 1
    return res


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
