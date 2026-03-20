import random as rd
import math
import copy
import json
import matplotlib

with open("nombres.json","r") as nom:
    listNmbr = json.load(nom)

   
#mira esto de aqui
# On definit le planète par son nom (composé de 2 noms), et ses coordonées
class Planete:
    def __init__(self,NomP: str, x: int, y: int): #__init__ sert à initialiser la classe pour pouvoir assigner les valeurs
        self.NomP = NomP
        self.x = x
        self.y = y
        
    
    def __repr__(self):
        #Sans ça c'est mort ça donne des caractèeres sombres et obscures
        # ! que hace repr? Es como ToString en Java
        return f"[{self.NomP} | Coordonnées: ({self.x}, {self.y})]"
        
class Galaxia: #GENERA LOS PLANETAS UNICAMENTE 

    def __init__(self):# Nassem: porque no lo pusistes en argulento a listPlnt?
        self.listPlnt: list[Planete] = []
        self.nombreCoplt : str
        self.coordx : int
        self.coordy : int
        self.NovoPlanete : Planete 

      #experimento a ver si funciona normalmente deberia de   de generarme unos 10 inidviduos
    def SamsungGalaxy(self,n: int):
        
        for i in range (1,n):
        
            rdint = rd.randint
            brandom = rdint(1,50) # dans le file Json on a 50 int avec chacun nom1 et nom2
            
            nombre1 = rd.choice(listNmbr)
            nombre2 = rd.choice(listNmbr)
             # on choisit un nom au hasard dans le file Json avec son id
            n1 = nombre1["nom1"]
            n2 = nombre2["nom2"]
            nombreCoplt = f"{n1} {n2}"
            
            coordx = rdint(1,28)*32 # la taille de la ventana y 32 porque los planetas son de 32 pixels
            coordy = rdint(1,21)*32
            
            NovoPlanete = Planete(nombreCoplt,coordx, coordy)
            
            self.listPlnt.append(NovoPlanete)
            CoordCurrentPlant = [coordx,coordy]
            PlantAntig = self.listPlnt [self.listPlnt.index(NovoPlanete)-1] # ! esto es para obtener el planeta anterior al nuevo planeta, pero no se si es la mejor forma de hacerlo
            

        return self.listPlnt 
    
    
#MEZCLA LA GALAXIA PARA OBTENER M ITINERARIOS DIFERENTES
class Itinerarios():
    def __init__(self, Galx : Galaxia):
        self.Galx = Galx
        self.distTot = 0

        self.itinerarios = []



    def mutation(self, p: int): # aqui los self.Galx.listPlnt[i] me dan errores del estilo No overloads for "__setitem__" match the provided arguments pero aun asi fucniona en main
        for i in self.Galx.listPlnt:
            if(rd.randint(0,100)<= p*100):#porque p*100 y cuando defines p, no veo que le hallas dado algun valor
                j = self.Galx.listPlnt[rd.randint(0, len(self.Galx.listPlnt)-1)]
                self.Galx.listPlnt[i], self.Galx.listPlnt[j] = self.Galx.listPlnt[j], self.Galx.listPlnt[i] # ! esto es para mezclar la lista de planetas, pero no se si es la mejor forma de hacerlo
    
    #MODIFS - PARA QUE SEA COMO EL PROBLEMA: EL PRIMER PLANETA ES EL MISMO PARA TODOS LOS ITINERARIOS, ASI QUE NO SE MEZCLA EL PRIMER PLANETA
    #generation aleatoire de m itineraires
    def genererRd(self, m: int):
        for i in range(m):
            # ! explicar para que esta copy | Bruh lo usastes y no sabias que era
            shuflPlnt = self.Galx.listPlnt.copy() #yo puse copy en las librerias porque lo qu hace es hacer una copia de las galxias y asi las poemos modificar sin problemas 
            rd.shuffle(shuflPlnt)
            self.itinerarios.append(shuflPlnt)

    #generation de m itineraires a partir de itinerarios existentes
    def genererHerit(self, i:int, m: int, p: int):
        for i in range(m):
            shuflPlnt = self.itinerarios[i]
            self.mutation(p)
            self.itinerarios.append(shuflPlnt)

    def Dist(self):# me da error me dice que NovoPlanete est un attributo desconocido pero si enciendo main no da errores
       if(self.Galx.listPlnt.index(self.Galx.NovoPlanete) > 0): #el primer index es 0 asi que  decimos que calcule las distancias solo cuandi haya mas de 1 planeta
            for i in range(len(self.Galx.listPlnt) - 1):# va parcorrir todo la lista y va coger el x y el y del primer planeta y del siguiente
                p1 = self.Galx.listPlnt[i]#guarda el primero
                p2 = self.Galx.listPlnt[i + 1]#
                dist = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) # ! esto es la formula de la distancia entre dos puntos en un plano cartesiano
                self.distTot += dist
            return self.distTot
        
#population es redundante con itinerios : eliminada 