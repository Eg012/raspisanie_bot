import random


class Train:
    def __init__(self, number, dest, time_train):
        self.dest = dest
        self.time_train = time_train
        self.number = number

    def __str__(self):
        return f'number: {self.number}, time: {self.time_train}, dest: {self.dest}'

    @staticmethod
    def random():
        tos = ['Туапсе', 'Сочи', 'Симферопаль']
        numbers = [1, 2, 3]
        time = f'{random.randint(0, 23)}:{random.randint(0, 59)} '
        return Train(dest=random.choice(tos),
                     number=random.choice(numbers),
                     time_train=time
                     )

    def __gt__(self, other):
        return self.number > other.number


trains = []
for i in range(5):
    trains.append(Train.random())




for i in sorted(trains):
    print(i)
