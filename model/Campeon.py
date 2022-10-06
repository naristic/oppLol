from .Personaje import Personaje
class Campeon(Personaje):
    __habilidad={}
    __objetos=[]
    __oro=0
    __nivel=1

    
    def __init__(self,nombre,tipoDaño,vida,verlAtaque,daño,habilidad,objetos,oro):
        Personaje.__init__(self=self,nombre=nombre,tipoDaño=tipoDaño,vida=vida,velAtaque=verlAtaque,daño=daño)
        self.__habilidad=habilidad
        self.__objetos=objetos
        self.__oro=oro
        
   