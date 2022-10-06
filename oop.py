#from model.Personaje import Personaje
from model.Campeon import Campeon

d ={'Q':200,'W':250,'E':200,'R':300}
l=[]
l2=[]

darius = Campeon(nombre='darius',tipoDaño='ap',vida=2000,verlAtaque=2.0,habilidad=d,objetos=l,oro=400)
l2.append(darius)
masterYi = Campeon(nombre='master yi',tipoDaño='ap',vida=2000,verlAtaque=2.0,habilidad=d,objetos=l,oro=400)
l2.append(masterYi)
print(darius.getNombre())
print(masterYi.getVida())
l2=darius.ataqueBasico(l2,masterYi)
print(l2[1].getVida())
#darius.ataqueBasico(masterYi)