import random


class Animal:
    def __init__(self, animal_weight):
        self.animal_weight = animal_weight

    def __int__(self):
        return self.animal_weight * 0.1  # animal_weight * 0.1


class Сarnivorous(Animal):
    def __init__(self, animal_weight, foot_count):
        super().__init__(animal_weight)
        self.foot_count = foot_count
        self.foot_type = "meat"

