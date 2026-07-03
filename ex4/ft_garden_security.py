#!/usr/bin/env python3

class Plant:
    def __init__(self, name:str, height:float=0.0, age:int=0) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_height(self) -> float:
        return round(self._height, 1)

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height:float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {int(self._height)}cm")

    def set_age(self, new_age:int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.name}: {rose.get_height()}cm, {rose.get_age()} days old\n")

    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-1.0)
    rose.set_age(-1)
    print()
    print(f"Current state: {rose.name}: {rose.get_height()}cm, {rose.get_age()} days old")

if __name__ == "__main__":
    main()
