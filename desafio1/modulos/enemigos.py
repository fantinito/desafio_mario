from modulos.personajes import Personaje

class Enemigo(Personaje):
    def __init__(self,posicion_x,posicion_y,dano):
        self.__dano=dano
        super().__init__(posicion_x,posicion_y,dano)
    
    def get_dano(self,dano):
        return self.__dano
    
    def atacar(self,ataque):
        print(f"lanza un ataque de {ataque}")
    