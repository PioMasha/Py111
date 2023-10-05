def counting(n, k):
    """
    Решение задачи Считалочка.

    :param n: Кол-во человек
    :param k: Кол-во слогов до выбывания
    :return: Номер последнего игрока
    """

    list_counting = list(range(1, n+1))  # список группы людей
    current = 0  # указатель на текущего игрока

    while len(list_counting) > 1:
        current = (current + k - 1) % len(list_counting)  # Вычисляем позицию выбывшего игрока
        list_counting.pop(current)  # Удаляем из списка группы людей выбывшего игрока

    return list_counting[0]


n = 16
k = 7
win = counting(n, k)
print("Номер последнего оставшегося человека:", win)
