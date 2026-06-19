#!/usr/bin/env python3

class Plant:
    def __init__(self, name:str, height:float, age:int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height = round(self.height + 0.8, 1)
        self.age += 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def main():
    height = 25.0
    rose = Plant("Rose", height, 30)

    print("=== Garden Plant Growth ===")

    for day in range(7):
        print(f"=== Day {day + 1} ===")
        rose.show()
        rose.grow()

    total_growth = round(rose.height - height, 1)

    print(f"Growth this week: {total_growth}cm")

if __name__ == "__main__":
    main()
