#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0.0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return round(self._height, 1)

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {int(self._height)}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def show(self) -> None:
        print(f"{self._name}: {self.get_height()}cm, {self.get_age()}", end="")
        print(" days old")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-1.0)
    rose.set_age(-1)
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
