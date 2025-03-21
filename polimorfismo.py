class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

def fazer_animal_falar(animal: Animal):
    print(animal.fazer_som())


cachorro = Cachorro()
gato = Gato()

#chama o método de cada animal de forma polifórmica
fazer_animal_falar(cachorro)
fazer_animal_falar(gato)
