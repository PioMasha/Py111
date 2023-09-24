from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1
    for j in range(m):
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + dp[i - 1][j - 1]

    return dp


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
