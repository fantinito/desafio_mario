from modulos.enemigos import Enemigo

class Koopa(Enemigo):
    def __init__(self,posicion_x, posicion_y,dano):
        super().__init__(posicion_x,posicion_y,dano)
        
    def volar(self):
        print("vuela")
