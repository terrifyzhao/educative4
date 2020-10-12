def diff_ways_to_evaluate_expression(input):
    result = []
    if '+' not in input and '-' not in input and '*' not in input:
        result.append(int(input))
    else:
        for i in range(len(input)):
            s = input[i]
            if not s.isdigit():
                left = diff_ways_to_evaluate_expression(input[:i])
                right = diff_ways_to_evaluate_expression(input[i + 1:])
                for l in left:
                    for r in right:
                        if s == '+':
                            result.append(l + r)
                        elif s == '-':
                            result.append(l - r)
                        elif s == '*':
                            result.append(l * r)

    return result


def main():
    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
