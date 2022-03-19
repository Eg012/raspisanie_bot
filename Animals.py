import random


class Animal:
    def __init__(self, animal_weight, eat_norma):
        self.animal_weight = animal_weight
        self.eat_norma = eat_norma

    def __int__(self):
        return int(self.animal_weight * self.eat_norma)

    @staticmethod
    def random(class_name, random_pool):
        return class_name(**random.choice(random_pool))


class Сarnivorous(Animal):
    def __init__(self, animal_weight, eat_norma, name, food_type=None):
        super().__init__(animal_weight, eat_norma)
        self.food_type = "meat" if food_type is None else food_type
        self.name = name

    def __str__(self):
        return f'класс животного:{self.__class__.__name__}, имя животного:{self.name}, тип еды:{self.food_type}, количество еды:{self.eat_norma}'

    @staticmethod
    def random():
        pool = [
            {
                "animal_weight": random.randint(60, 120),
                "eat_norma": 1.5,
                "name": "гепард"
            },
            {
                "animal_weight": random.randint(100, 400),
                "eat_norma": 5.6,
                "name": "медведь"
            },
            {
                "animal_weight": random.randint(150, 400),
                "eat_norma": 7.0,
                "name": "морж"
            }
        ]
        return Animal.random(Сarnivorous, pool)


class Omnivorous(Animal):
    def __init__(self, animal_weight, name):
        super().__init__(animal_weight)
        self.foot_type = "food"
        self.name = name

    @staticmethod
    def random():
        pool = [
            {
                "animal_weight": random.randint(4, 15),
                "eat_norma": 1.5,
                "name": "барсук"
            },
            {
                "animal_weight": random.randint(3, 8),
                "eat_norma": 1.0,
                "name": "утка"
            },
            {
                "animal_weight": random.randint(50, 150),
                "eat_norma": 7.0,
                "name": "кабан"
            }
        ]
        return Animal.random(Omnivorous, pool)


class Herbivorous(Animal):
    def __init__(self, animal_weight, ):
        super().__init__(animal_weight)
        self.foot_type = "grass"

    @staticmethod
    def random():
        pool = [
            {
                "animal_weight": random.randint(10, 100),
                "eat_norma": 2.0,
                "name": "жираф"
            },
            {
                "animal_weight": random.randint(100, 220),
                "eat_norma": 5.6,
                "name": "панда"
            },
            {
                "animal_weight": random.randint(50, 150),
                "eat_norma": 7.0,
                "name": "зебра"
            }
        ]
        return Animal.random(Herbivorous, pool)


# animal_carnivorous = ['гепард', 'медведь', 'морж']
#         animal_herbivorous = ['Жираф', 'пандa , 'зебра']
#         animal_omnivorous = ['барсук', 'утка', 'кабан']
#         animal_type = ['carnivorous', 'omnivorous', 'herbivorous']
#         animal_weight = [random.randint(1,100)]

print(int(Сarnivorous.random()))
