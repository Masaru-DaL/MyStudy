def plus(i, j):
    """
    >>> plus(1, 1)
    2
    """
    return i + j


def main():
    for i in range(100000):
        i = plus(i, i)


if __name__ == "__main__":
    import doctest

    doctest.testmod()  # 埋め込まれたテストを自動検証する
