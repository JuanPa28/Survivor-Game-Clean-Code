class Weapon:
    def __init__(self, symbol, damage, name):
        """
        Inicia una instancia de arma con símbolo, daño y nombre específicos.

        Parámetros:
        symbol (str): Símbolo que representa el arma en el juego.
        damage (int): Valor de daño que causa el arma.
        name (str): Nombre del arma.
        """
        self.symbol = symbol
        self.damage = damage
        self.name = name
