#!/usr/bin/env python3

class Plant:
    def __init__(self, name:str, height:int, age:int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def main():
	garden = [
		Plant("Rose", 25, 30),
		Plant("Tulip", 15, 20),
		Plant("Lily", 40, 45)
	]

	print("=== Garden Plant Registry ===")

	for plant in garden:
		plant.show()

if __name__ == "__main__":
	main()
