"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError("массив пуст")

    min_value = float('inf')
    min_index = None

    for index in range(len(arr)):
        element = arr[index]
        if element < min_value:
            min_value = element
            min_index = index

    if min_index is not None:
        return min_index
    else:
        raise ValueError("Массив пуст")
