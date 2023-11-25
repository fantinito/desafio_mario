from modulos.personajes import Personaje

class Mario(Personaje):
    def __init__(self, nombre, posicion_x, posicion_y, vidas):
        super().__init__(nombre,posicion_x,posicion_y, vidas)

        
    def lanzar_fuego(self):
        print("lanza fuego")

   