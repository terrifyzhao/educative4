def find_happy_number(num):
    slow, fast = num, num

    while 1:
        slow = calculate(slow)
        fast = calculate(calculate(fast))
        if slow == fast:
            return False
        if slow == 1 or fast == 1:
            return True


def calculate(num):
    res = 0
    while num:
        n = num % 10
        res += n * n
        num = num // 10
    return res


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
