class Forma:
    def dibujar(self):
        print("Dibujando forma")

class Color:
    def __init__(self, color):
        self.color = color

    def pintar(self):
        print(f"Pintando con {self.color}")

class CuadradoColorido(Forma, Color):
    def __init__(self, color, lados):
        Forma.__init__(self)  # Llamando al constructor de la clase Forma
        Color.__init__(self, color)  # Llamando al constructor de la clase Color
        self.lado = lados

    def dibujar_y_pintar(self):
        super().dibujar()  # Llamando al metodo dibujar de la clase Forma usando super()
        super().pintar()   # Llamando al metodo pintar de la clase Color usando super()

# Creando una instancia de CuadradoColorido
cuadrado = CuadradoColorido(lados=4, color="rojo")

cuadrado.dibujar_y_pintar()
