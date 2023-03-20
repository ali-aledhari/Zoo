from animal import Animal

class Zoo:
    def __init__(self, animals):
        self._animals = animals

    @property
    def animals(self):
        return self._animals

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Can only add instances of Animal to the zoo.")
        self._animals.append(animal)

    def __add__(self, other):
        if isinstance(other, Zoo):
            return Zoo(self._animals + other.animals)
        else:
            raise TypeError("The addition is only possible between two zoos.")
