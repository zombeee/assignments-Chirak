



def rabbits_population(month: int, litter: int) -> int:
    """
    Counts the size of the rabbit population with the given litter
    in the given month if population starts with one pair
    :param month: age of population
    :param litter: given letter for this population
    :return: size of the population on the given month
    """
    fib_1, fib_2 = 2, 2 + litter
    for _ in range(month-2):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

rabbits_population(5, 2)