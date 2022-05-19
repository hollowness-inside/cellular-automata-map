from dataclasses import dataclass
from random import seed, randbytes
from typing import Any, List, Tuple


@dataclass
class _MapData:
    width:  int
    height: int
    seed:   Any
    ratio:  int
    smooth: int


def generate(size: Tuple[int, int], rseed: Any = 0, ratio: int = 127, smooth: int = 5) -> List[int]:
    width, height = size
    data = _MapData(width, height, rseed, ratio, smooth)

    seed(rseed)
    arr = randbytes(width * height)
    arr = [(i >= ratio and 1 or 0) for i in arr]

    for _ in range(smooth):
        _smooth(arr, data)

    return arr


def _smooth(arr: List[int], md: _MapData):
    for y in range(md.height):
        for x in range(md.width):
            surr = _count_surrounding(x, y, arr, md)

            if surr > 4:
                arr[y*md.width + x] = 1
            elif surr < 4:
                arr[y*md.width + x] = 0


def _count_surrounding(x: int, y: int, arr: List[int], md: _MapData) -> int:
    count = 0

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == dy == 0:
                continue

            if _get(x+dx, y+dy, arr, md) == 1:
                count += 1

    return count


def _get(x: int, y: int, arr: List[int], md: _MapData) -> int:
    if not ((0 < x < md.width) and (0 < y < md.height)):
        return 1

    return arr[y * md.width + x]
