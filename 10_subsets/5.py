class Parentheses:
    def __init__(self, content, open, close):
        self.close = close
        self.open = open
        self.content = content


from collections import deque


def generate_valid_parentheses(num):
    result = []

    queue = deque()
    queue.append(Parentheses('', 0, 0))

    while queue:
        p = queue.popleft()
        if p.open == p.close == num:
            result.append(p.content)
        else:
            if p.open < num:
                queue.append(Parentheses(p.content + '(', p.open + 1, p.close))
            if p.close < p.open:
                queue.append(Parentheses(p.content + ')', p.open, p.close + 1))

    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
