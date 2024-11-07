class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health


    def introduce(self):
        print(f"Я: {self.name}, мое здоровье: {self.health}")


    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает и восстанавливает здоровье, мое новое здоровье: {self.health}")

    def action(self):
        print(f"{self.name} выполняет базовое действие: делает ход\n")


