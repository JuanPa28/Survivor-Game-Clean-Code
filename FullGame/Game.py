import random
import keyboard

from Player import Player
from Monster import Monster
from Weapon import Weapon
from Food import Food

from Camera import Camera


class Game:
    def __init__(self, size):
        self.size = size
        self.player = Player(self)
        self.monster = Monster(self)
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.place_random_objects()
        self.camera = Camera()

    def place_random_objects(self):
        # Coloca objetos aleatorios (comida y armas) en el mapa
        self.place_random_food()
        self.place_random_weapons()

    def place_random_food(self):
        food = ["[🍩]"]
        # Coloca comida aleatoriamente en el mapa
        num_food = random.randint(1 , self.size * 2)
        for _ in range(num_food):
            x = random.randint(1, self.size - 1)
            y = random.randint(1, self.size - 1)
            self.grid[x][y] = Food(random.choice(food))

    def place_random_weapons(self):
        weapons = ["[🔫]", "[🏹]", "[🩼]", "[💉]"]
        weapons_damages = [25, 35, 20, 30]
        weapons_names = ["Pistola", "Arco", "Muleta", "Veneno"]
        # Coloca armas aleatoriamente en el mapa
        for i in range(len(weapons)):
            x = random.randint(1, self.size - 1)
            y = random.randint(1, self.size - 1)
            self.grid[x][y] = Weapon(weapons[i], weapons_damages[i], weapons_names[i])

    def play(self):
        # Ciclo principal del juego
        while self.player.is_alive() and self.monster.is_alive():
            self.print_game_state()
            self.player_turn()
            self.monster_turn()

        self.print_game_state()

        if self.player.is_alive():
            print("FELICIDADES!!! Ganaste el juego.")
        else:
            print("GRAVE... EL monstruo te derrotó, perdiste el juego.")

    def print_game_state(self):
        # Imprime el estado actual del juego
        print("PH PLAYER =", self.player.health, "Inventario =", [item.name for item in self.player.inventory])
        print("Inventario de curaciones: ", [item.symbol for item in self.player.inventory_food])
        print("PH Monstruo =", self.monster.health)
        print("Mapa:")
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if self.player.x == i and self.player.y == j:
                    print(self.player.symbol, end=" ")
                elif self.monster.x == i and self.monster.y == j:
                    print(self.monster.symbol, end=" ")
                elif cell is None:
                    print("[ ]", end=" ")
                else:
                    print(cell.symbol, end=" ")
            print()

    def player_turn(self):
        # Turno del jugador
        valid_actions = ["comer", "atacar", "derecha", "izquierda", "arriba", "abajo"]
        action = self.get_player_action(valid_actions)
        if action == "derecha":
            self.move_player(action)
        elif action == "izquierda":
            self.move_player(action)
        elif action == "arriba":
            self.move_player(action)
        elif action == "abajo":
            self.move_player(action)
        elif action == "comer":
            if self.player.inventory_food:
                self.player.eat_food()
            else:
                print("GRAVE...No tienes curación")
        elif action == "atacar":
            if self.player.x == self.monster.x and (
                    self.player.y - self.monster.y == -1 or self.player.y - self.monster.y == 1):
                self.player.attack_monster(self.monster)
            elif self.player.y == self.monster.y and (
                    self.player.x - self.monster.x == -1 or self.player.x - self.monster.x == 1):
                self.player.attack_monster(self.monster)
            else:
                print("Debes estar adyacente al monstruo para atacarlo")

    def get_player_action(self, valid_actions):
        # Obtiene la acción seleccionada por el jugador
        while True:
            if keyboard.is_pressed('space'):
                action = self.camera.proceso()
                if action in valid_actions:
                    return action
                print("Acción inválida. Intenta nuevamente.")

    def move_player(self, direction):
        # Mueve al jugador en la dirección especificada
        delta_x, delta_y = self.get_movement_delta(direction)
        new_x = self.player.x + delta_x
        new_y = self.player.y + delta_y

        if self.is_valid_position(new_x, new_y):
            self.player.x = new_x
            self.player.y = new_y
            self.resolve_encounter()
        else:
            print("Movimiento inválido. Intenta nuevamente.")

    def get_movement_delta(self, direction):
        # Devuelve el cambio en las coordenadas x e y para la dirección especificada
        if direction == "arriba":
            return (-1, 0)
        elif direction == "abajo":
            return (1, 0)
        elif direction == "izquierda":
            return (0, -1)
        elif direction == "derecha":
            return (0, 1)

    def is_valid_position(self, x, y):
        # Verifica si la posición especificada es válida dentro del mapa
        return 0 <= x < self.size and 0 <= y < self.size

    def resolve_encounter(self):
        # Resuelve el encuentro entre el jugador y el objeto/monstruo en su posición actual
        object_at_position = self.grid[self.player.x][self.player.y]

        if isinstance(object_at_position, Food):
            self.player.inventory_food.append(self.grid[self.player.x][self.player.y])
            self.grid[self.player.x][self.player.y] = None
        elif isinstance(object_at_position, Weapon):
            self.player.inventory.append(self.grid[self.player.x][self.player.y])
            self.grid[self.player.x][self.player.y] = None
        elif isinstance(object_at_position, Monster):
            self.player.attack_monster(self.monster)

    def monster_turn(self):
        # Turno del monstruo
        self.monster.move_randomly()
        if self.monster.x == self.player.x and self.monster.y == self.player.y:
            self.monster.attack_player(self.player)

game = Game(5)
game.play()