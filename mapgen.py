from random import seed, randbytes
from typing import Any, List, Tuple


def generate(size: Tuple[int, int], rseed: Any = 0, ratio: int = 127, smooth: int = 5) -> List[int]:
    width, height = size

    seed(rseed)
    arr = randbytes(width * height)
    arr = [(i >= ratio and 1 or 0) for i in arr]

    for _ in range(smooth):
        _smooth(arr, size)

    return arr


def _smooth(arr: List[int], size: Tuple[int, int]):
    for y in range(size[1]):
        for x in range(size[0]):
            surr = _count_surrounding(x, y, arr, size)

            if surr > 4:
                arr[y*size[0] + x] = 1
            elif surr < 4:
                arr[y*size[0] + x] = 0


def _count_surrounding(x: int, y: int, arr: List[int], size: Tuple[int, int]) -> int:
    count = 0

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == dy == 0:
                continue

            if _get(x+dx, y+dy, arr, size) == 1:
                count += 1

    return count


def _get(x: int, y: int, arr: List[int], size: Tuple[int, int]) -> int:
    if not ((0 < x < size[0]) and (0 < y < size[1])):
        return 1

    return arr[y * size[0] + x]
