def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n < 0:
        raise ValueError("Факториал должен быть целым числом")

    result = 1
    for i in range(1, n+1):
        result *= i
    return result
