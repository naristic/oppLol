


class Personaje:
    __nombre=''
    __tipoDaño=''
    __vida=0
    __velAtaque=0
    __armadura=0
    __resMagica=0
    __daño=0


    def __init__(self,nombre,tipoDaño,vida,velAtaque,daño) :
        self.__nombre = nombre
        self.__tipoDaño = tipoDaño
        self.__vida = vida
        self.__velAtaque = velAtaque
        self.__daño = daño
        
    
        

    def getNombre(self):
        return self.__nombre

    def getVida(self):
        return self.__vida

    def setVida(self,n):
        self.__vida=int(n)

    def ataqueBasico(self,d,n):
        
        for i in range(len(d)):
            if d[i].getNombre()==n.getNombre():
                d[i].setVida(d[i].getVida()-self.__daño)
                
        return d
    