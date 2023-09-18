def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    stack = []

    brackets_pairs = {')': '(', '}': '{', ']': '['}
    for symbol in brackets_row:
        if symbol in brackets_pairs.values():
            stack.append(symbol)
        elif symbol in brackets_pairs.keys():
            if not stack or stack.pop() != brackets_pairs[symbol]:
                return False
    return not stack


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
