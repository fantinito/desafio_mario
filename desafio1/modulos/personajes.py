class Personaje:
    def __init__(self,nombre,posicion_x, posicion_y, vidas):
        self.__nombre= nombre
        self.__posicion_x= posicion_x
        self.__posicion_y= posicion_y
        self.__vidas= vidas
        
    def get_nombre(self):
        return self.__nombre
    
    def get_posicion_x(self):
        return self.__posicion_x
    
    def get_posicion_y(self):
        return self.__posicion_y
    
    def get_vidas(self):
        return self.__vidas
        
    def mover(self,x,y):
        self.__posicion_x=x
        self.__posicion_y=y
        print(f"Mover a la posicion x {self.__posicion_x} y: {self.__posicion_y}")
        
        
    def saltar(self):
        print("saltó")
    
    def caer(self):
        print("se cayó")        
        