class Animal:
    def hacer_sonido(self):
        return[]

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

class Mono(Animal):
    def hacer_sonido(self):
        return "¡Hu Hu Ha Ha!"

# Ejemplo 
if __name__ == "__main__":
    perro = Perro()
    gato = Gato()
    mono = Mono ()

    print("El perro hace: " + perro.hacer_sonido())
    print("El gato hace: " + gato.hacer_sonido())
    print("El mono hace: " + mono.hacer_sonido())

