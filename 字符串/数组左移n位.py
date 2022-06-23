from typing import List, Any


def func(array: List[Any], n: int):
    """
    反转3次
    """
    def _reverse(a: List[Any], start: int, end: int):
        i, j = start, end - 1
        while i < j:
            a[i], a[j] = a[j], a[i]
            i, j = i + 1, j - 1

    _reverse(array, 0, n)
    _reverse(array, n, len(array))
    _reverse(array, 0, len(array))


if __name__ == '__main__':
    array = [1, 2, 3, 4]
    func(array, 2)
    print(array)
