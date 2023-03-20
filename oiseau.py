from animal import Animal

class Oiseau(Animal):
    def __init__(self, poids, taille, altitude_max):
        super().__init__(poids, taille)
        self._altitude_max = altitude_max

    def se_deplacer(self):
        print("Je vole")

    @property
    def altitude_max(self):
        return self._altitude_max

    @altitude_max.setter
    def altitude_max(self, value):
        if value < 0:
            raise ValueError("Altitude cannot be negative")
        self._altitude_max = value

    def __str__(self):
        return f"Oiseau: poids={self._poids}, taille={self._taille}, altitude_max={self._altitude_max}"
