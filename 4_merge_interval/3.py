def merge(intervals_a, intervals_b):
    result = []
    i, j = 0, 0

    while i < len(intervals_a) and j < len(intervals_b):
        a_over_b = intervals_a[i][0] <= intervals_b[j][0] <= intervals_a[i][1]
        b_over_a = intervals_b[j][0] <= intervals_a[i][0] <= intervals_b[j][1]

        if a_over_b or b_over_a:
            result.append([max(intervals_a[i][0], intervals_b[j][0]),
                           min(intervals_a[i][1], intervals_b[j][1])])

        if intervals_a[i][1] < intervals_b[j][1]:
            i += 1
        else:
            j += 1

    return result


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
