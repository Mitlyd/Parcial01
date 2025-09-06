#AI-TRAP:OOP

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

r = Rectangulo(3, 4)
print(r.area())
