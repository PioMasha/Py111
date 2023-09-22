def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if isinstance(type(n), float) or n < 0:
        raise ValueError("Факториал должен быть положительным числом")

    if n == 0:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    n = 5
    fact = factorial_recursive(n)
    print(f"Факториал числа {n} равен {fact}")