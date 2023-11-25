from modulos.enemigos import Enemigo

class Goomba(Enemigo):
    def __init__(self,posicion_x, posicion_y,dano):
        super().__init__(posicion_x,posicion_y,dano)
        
    def escudo(self):
        print("activa un escudo protector")