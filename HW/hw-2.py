from main import Hero


class Warrior(Hero):
    def __init__(self, name, health=200, fury=100):
        super().__init__(name, health)
        self.fury = fury


    def attack(self):
        if self.fury >= 10:
            self.fury -=10
            return f"{self.name} атакует!! Оставшаяся ярость: {self.fury}"
        else:
            return f"{self.name}, не достаточно ярости для атаки"


    def action(self):
        base_action = super().action()
        spell_result = self.attack()
        return f"{base_action} {spell_result}"


def hero_action(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())


warrior = Warrior("Ингвар", 250, 50)

hero_action(warrior)