#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def display(self, plant_name: str) -> None:
            print(f"[statistics for {plant_name}]")
            print(f"Stats:{self.__grow_count} grow, "
                  f"{self.__age_count} age, "
                  f"{self.__show_count} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._stats: Plant._Stats = Plant._Stats()

    def grow(self, height_increase: float = 8.0):
        self._stats.increment_grow()
        self._height += height_increase

    def age(self):
        self._stats.increment_age()
        self._age += 1

    def show(self):
        self._stats.increment_show()
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")

    @staticmethod
    def is_older_than_year(age_days):
        return age_days > 365


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._blooming: bool = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def grow(self) -> None:
        super().grow(8.0)

    def bloom(self) -> None:
        self._blooming: bool = True


class Tree(Plant):
    class _TreeStats:
        def __init__(self) -> None:
            self._shade_count: int = 0

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter
        self._tree_stats: Tree._TreeStats = Tree._TreeStats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose._stats.display(rose._name)
    print(f"[asking the {rose._name} to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    rose._stats.display(rose._name)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak._stats.display(oak._name)


if __name__ == "__main__":
    main()
