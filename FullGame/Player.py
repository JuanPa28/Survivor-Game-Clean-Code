import random

class Player:
    def __init__(self, game):
        """
        Inicia una instancia de jugador en una posición aleatoria dentro del juego.

        Parámetros:
        game (Game): Instancia del juego al que pertenece el jugador.
        """
        self.x = random.randint(0, game.size - 1)
        self.y = random.randint(0, game.size - 1)
        self.health = 10
        self.inventory = []
        self.inventory_food = []
        self.symbol = "[🧑]"

    def is_alive(self):
        """
        Verifica si el jugador sigue vivo.

        Retorna:
        bool: True si el jugador tiene salud mayor que 0, de lo contrario False.
        """
        return self.health > 0

    def eat_food(self):
        """
        Permite al jugador comer un elemento de comida, aumentando su salud en 10 puntos.
        """
        self.health += 10
        self.inventory_food.pop(0)

    def attack_monster(self, monster):
        """
        Permite al jugador atacar al monstruo utilizando un arma del inventario.

        Parámetros:
        monster (Monster): Instancia del monstruo atacado.
        """
        if self.inventory:
            weapon = self.inventory.pop(0)
            monster.health -= weapon.damage
            print("¡Golpeaste al monstruo con", weapon.name, "y le quitaste", weapon.damage, "de vida!")
        else:
            print("¡No tienes armas para atacar al monstruo, consigue una!")
