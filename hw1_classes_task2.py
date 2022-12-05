class Bottle:
    color = ''
    contains = 0.0

    def __init__(self):
        self.contains = int(self.contains)

    def get_content(self):
        return self.contains

    def fill(self, volume):
        self.contains = self.contains + volume
        return self.contains


bottle_1 = Bottle()
bottle_2 = Bottle()
bottle_1.color = 'Красная'
bottle_2.color = 'Синяя'
print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())
print(bottle_2.color, bottle_2.get_content())
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_content())
