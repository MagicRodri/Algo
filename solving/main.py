def remove_duplicate(arr: list) -> list:
    """
    Remove duplicate from a list
    :param arr:
    :return:
    """
    return list(set(arr))


if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(remove_duplicate(sample))