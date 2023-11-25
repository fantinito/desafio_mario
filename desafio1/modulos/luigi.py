from modulos.personajes import Personaje

class Luigi(Personaje):
    def __init__(self, nombre, posicion_x, posicion_y, vidas):
        super().__init__(nombre,posicion_x,posicion_y, vidas)

    def lanzar_honguitos(self):
        print("lanza honguitos")



