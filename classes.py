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
        
    # lo definimos aqui para llamarlo en itinéraire
    
    def __repr__(self):
        #Sans ça c'est mort ça donne des caractèeres sombres et obscures
        # ! que hace repr? Es como ToString en Java
        return f"[{self.NomP} | Coordonnées: ({self.x}, {self.y})]"
        
class Galaxia:
    
    def __init__(self, listPlnt:Planete):
        self.listPlnt = listPlnt
     
      #experimento a ver si funciona normalmente deberia de   de generarme unos 10 inidviduos
    def SamsungGalaxy(self,n: int):# ! puse el tipo aqui tambien por coherencia, falta testearlo 
        for i in range (1,n):
            self.listPlnt 
            
        
            rdint = rd.randint
            brandom = rdint(1,50) # dans le file Json on a 50 int avec chacun nom1 et nom2
            
            nombre = rd.choice(listNmbr) # on choisit un nom au hasard dans le file Json avec son id
            nombre1 = nombre["nom1"]
            nombre2 = nombre["nom2"]
            nombreCoplt = f"{nombre1} {nombre2}"
            
            coordx = rdint(1,28)*32 # la taille de la ventana y 32 porque los planetas son de 32 pixels
            coordy = rdint(1,21)*32
            
            NovoPlanete = Planete(nombreCoplt,coordx, coordy)
            
            self.listPlnt .append(NovoPlanete)
            CoordCurrentPlant = [coordx,coordy]
            PlantAntig = self.listPlnt [self.listPlnt.index(NovoPlanete)-1] # ! esto es para obtener el planeta anterior al nuevo planeta, pero no se si es la mejor forma de hacerlo
            

        return self.listPlnt 
    
    
    
class Itinerario():
    def __init__(self, Galx : Galaxia, distTot : int):
        self.Galx = Galx
        self.distTot = distTot
    def Dist(self):
       if(self.Galx.listPlnt.index(self.Galx.NovoPlanete) > 0): #el primer index es 0 asi que  decimos que calcule las distancias solo cuandi haya mas de 1 planeta
            for i in range(len(self.Galx.listPlnt) - 1):# va parcorrir todo la lista y va coger el x y el y del primer planeta y del siguiente
                p1 = self.Galx.listPlnt[i]#guarda el primero
                p2 = self.Galx.listPlnt[i + 1]#
                dist = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) # ! esto es la formula de la distancia entre dos puntos en un plano cartesiano
                self.distTot += dist
            return self.distTot
    

        
#population sera l'ensemble d'itineraires 
class Population:
    def __init__(self):
        pass # ! esto es para reiniciar? o para que sirve?
