from animal import Animal
from serpent import Serpent
from oiseau import Oiseau
from zoo import Zoo

ani = Animal(10, 20)
print(ani)
ani.se_deplacer()

s = Serpent(5, 10)
print(s)
s.se_deplacer()

o = Oiseau(1, 5, 100)
print(o)
o.se_deplacer()

zoo1 = Zoo([ani, s])
zoo2 = Zoo([o])
zoo3 = zoo1 + zoo2
for animal in zoo3.animals:
    print(animal)

