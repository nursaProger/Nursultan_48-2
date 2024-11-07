class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city



    def introduce(self):
        print(f"Привет, меня зовут {self.name},"
                f" мне {self.age} лет, я живу в {self.city}")



    def is_adult(self):
        if self.age >= 18:
            return print("True")
        else:
            return print("False")



    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Город: {self.city}'

        



person = Person("Carl", 20, "Boston")
person.introduce()


leon = Person("Leon", 18, "Moscow")
leon.is_adult()

alice = Person("Alice", 16, "London")
alice.is_adult()

dastan = Person("Dastan", 24, "Bishkek")
dastan.is_adult()

print(person)


