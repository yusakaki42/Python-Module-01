#!/usr/bin/env python3

class Plant:
    def __init__(self, name:str, height:float, age:int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_height(self) -> float:
        return round(self._height, 1)

    def set_age(self) -> int:
        return self._age

    def get_height(self, new_height:float) -> None:
        if self._height < 0.0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def get_age(self, new_age:int) -> None:
        if self._age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")

if __name__ == "__main__":
    main()
