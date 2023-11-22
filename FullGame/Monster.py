import random

class Monster:
    def __init__(self, game):
        """
        Inicia una instancia de monstruo en una posición aleatoria dentro del juego.

        Parámetros:
        game (Game): Instancia del juego al que pertenece el monstruo.
        """
        self.game = game
        self.x = random.randint(0, game.size - 1)
        self.y = random.randint(0, game.size - 1)
        self.health = 100
        self.symbol = "[👻]"

    def is_alive(self):
        """
        Verifica si el monstruo sigue vivo.

        Retorna:
        bool: True si el monstruo tiene salud mayor que 0, de lo contrario False.
        """
        return self.health > 0

    def move_randomly(self):
        """
        Mueve al monstruo en una dirección aleatoria dentro del juego.
        """
        directions = ["arriba", "abajo", "izquierda", "derecha"]
        direction = random.choice(directions)
        delta_x, delta_y = self.game.get_movement_delta(direction)  # Usar "self.game.get_movement_delta"
        new_x = self.x + delta_x  # Calcular las nuevas coordenadas sin modificar las actuales
        new_y = self.y + delta_y

        if self.game.is_valid_position(new_x, new_y):  # Usar "self.game.is_valid_position"
            self.x = new_x  # Asignar las nuevas coordenadas
            self.y = new_y

    def attack_player(self, player):
        """
        Ataca al jugador y reduce su salud en 25 puntos.

        Parámetros:
        player (Player): Instancia del jugador atacado.
        """
        player.health -= 25
        print("¡CORREEEE, el monstruo te quitó 25 de vida!")
