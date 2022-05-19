from random import seed, randbytes
from typing import Any, List, Tuple


class MapGen:
    width:  int
    height: int
    ratio:  int
    smooth: int
    seed:   Any
    array:  List[int]

    def __init__(self, size: Tuple[int, int], rand_seed: Any = 0, ratio: int = 127, smooth: int = 5):
        self.width, self.height = size
        self.seed = rand_seed
        self.ratio = ratio
        self.smooth = smooth
        self.array = [0 for _ in range(size[0] * size[1])]

    def generate(self) -> List[int]:
        seed(self.seed)
        self.array = randbytes(self.width * self.height)
        self.array = [(i >= self.ratio and 1 or 0) for i in self.array]

        for _ in range(self.smooth):
            self._smooth()

        return self.array

    def _smooth(self):
        for y in range(self.height):
            for x in range(self.width):
                surr = self._count_surrounding(x, y)
                # print(surr)

                if surr > 4:
                    self.array[y*self.width + x] = 1
                elif surr < 4:
                    self.array[y*self.width + x] = 0

    def _count_surrounding(self, x: int, y: int) -> int:
        count = 0

        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == dy == 0:
                    continue

                if self._get(x+dx, y+dy) == 1:
                    count += 1

        return count

    def _get(self, x: int, y: int) -> int:
        if not ((0 < x < self.width) and (0 < y < self.height)):
            return 1

        return self.array[y * self.width + x]


def mapgen(size: Tuple[int, int],
           rand_seed: Any = 0,
           ratio: int = 130,
           smooth: int = 5) -> List[int]:
    """Wrapper for the MapGen class. Generates a new map and returns its data."""
    mg = MapGen(size, rand_seed, ratio, smooth)
    return mg.generate()
