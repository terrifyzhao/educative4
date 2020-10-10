def backspace_compare(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1

    while index1 >= 0 or index2 >= 0:
        n1 = next_index(str1, index1)
        n2 = next_index(str2, index2)

        if n1 < 0 and n2 < 0:
            return True
        if n1 < 0 or n2 < 0:
            return False
        if str1[n1] != str2[n2]:
            return False

        index1 = n1 - 1
        index2 = n2 - 1
        
    return True


def next_index(str, index):
    space_count = 0
    while index >= 0:
        if str[index] == '#':
            space_count += 1
        elif space_count > 0:
            space_count -= 1
        else:
            break
        index -= 1
    return index


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
