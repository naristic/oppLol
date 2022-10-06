from .Personaje import Personaje
class Campeon(Personaje):
    __habilidad={}
    __objetos=[]
    __oro=0

    
    def __init__(self,nombre,tipoDaño,vida,verlAtaque,habilidad,objetos,oro):
        Personaje.__init__(self=self,nombre=nombre,tipoDaño=tipoDaño,vida=vida,velAtaque=verlAtaque)
        self.__habilidad=habilidad
        self.__objetos=objetos
        self.__oro=oro
        
   