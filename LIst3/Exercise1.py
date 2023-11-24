def print_name(name, surname):
    print(f"Full name: {name} {surname}")

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_name(self):
        print(f"Full name: {self.name} {self.surname}")

name = input('Digite o seu nome: ')
surname = input('Digite o seu sobrenome: ')

person = Person(name, surname)
person.print_name()