#! /usr/bin/env python3


def change_giver(coins, change):
    """
    This function search minimal number of coins of given nominal to give change
    :type coins: collections.Sequence
    :param coins: sequence of coin nominals in increasing order
    coins must contain nominal == 1
    :type change: int
    :param change: How much money we need to give
    :return: List of coins
    :rtype: list
    """
    #  note: Subtask matrix has one extra row for empty subsequences
    subtasks_matrix = ([[0] * (change + 1) for
                       _ in range(0, len(coins))])
    for j in range(change+1):  # Initialization of first row
        subtasks_matrix[0][j] = j
    solution = []
    for i in range(1, len(coins)):
        for j in range(0, change+1):
            subtasks_matrix[i][j] = (subtasks_matrix[i-1][j]
                                     if subtasks_matrix[0][j] - coins[i] < 0
                                     else
                                     min(subtasks_matrix[i-1][j],
                                         subtasks_matrix[i][j-1]+1,
                                         subtasks_matrix[i][j-coins[i]]+1))
    while i and j:
        if subtasks_matrix[i][j] == subtasks_matrix[i-1][j]:
            i -= 1
        elif subtasks_matrix[i][j] == subtasks_matrix[i][j-1] + 1:
            j -= 1
            solution.append(1)
        else:
            solution.append(coins[i])
            j -= coins[i]
    return sorted(solution)


def test_change():
    change_giver([1, 4, 6, 10], 18)


def main():
    test_change()


if __name__ == '__main__':
    main()
