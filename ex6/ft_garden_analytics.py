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
            print(f"Stats:{self._grow_count} grow, "
                  f"{self._age_count} age, "
                  f"{self._show_count} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._stats: Plant._Stats = Plant._Stats()

    def grow(self, height_increase: float = 8.0):
        self._stats.increment_grow()
        self._height += height_increase

    def age(self, age_increase: int = 1):
        self._stats.increment_age()
        self._age += age_increase

    def show(self):
        self._stats.increment_show()
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age}", end="")
        print(" days old")

    @staticmethod
    def is_older_than_year(age_days):
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def grow(self, height_increase: float = 8.0) -> None:
        super().grow(height_increase)

    def bloom(self) -> None:
        self._blooming = True


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def increment_shade(self) -> None:
            self._shade_count += 1

        def display(self, plant_name: str) -> None:
            super().display(plant_name)
            print(f" {self._shade_count} shade")

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter
        self._stats: Tree._TreeStats = Tree._TreeStats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats.increment_shade()
        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and"
              f"{self._trunk_diameter}cm wide.")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds: int = 0

    def grow(self, height_increase: float = 30.0) -> None:
        super().grow(height_increase)

    def age(self, age_increase: int = 20) -> None:
        super().age(age_increase)

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def display(self, plant_name: str) -> None:
        self._stats.display(plant_name)


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
    print(f"[asking the {oak._name} to produce shade]")
    oak.produce_shade()
    oak._stats.display(oak._name)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print(f"[make {sunflower._name.lower()} grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    sunflower.display(sunflower._name)
    print()

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    unknown._stats.display(unknown._name)


if __name__ == "__main__":
    main()
