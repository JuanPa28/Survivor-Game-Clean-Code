import random

class Player:
    def __init__(self, game):
        self.x = random.randint(0, game.size - 1)
        self.y = random.randint(0, game.size - 1)
        self.health = 10
        self.inventory = []
        self.inventory_food = []
        self.symbol = "[🧑]"

    def is_alive(self):
        return self.health > 0

    def eat_food(self):
        self.health += 10
        self.inventory_food.pop(0)

    def attack_monster(self, monster):
        if self.inventory:
            weapon = self.inventory.pop(0)
            monster.health -= weapon.damage
            print("¡Golpeaste al monstruo con", weapon.name, "y le quitaste", weapon.damage, "de vida!")
        else:
            print("¡No tienes armas para atacar al monstruo, consigue una!")