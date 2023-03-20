class Animal:
    def __init__(self, poids, taille):
        self._poids = poids
        self._taille = taille

    def se_deplacer(self):
        pass

    @property
    def poids(self):
        return self._poids

    @poids.setter
    def poids(self, value):
        if value < 0:
            raise ValueError("Poids cannot be negative")
        self._poids = value

    @property
    def taille(self):
        return self._taille

    @taille.setter
    def taille(self, value):
        if value < 0:
            raise ValueError("Taille cannot be negative")
        self._taille = value

    def __str__(self):
        return f"Animal: poids={self._poids}, taille={self._taille}"
