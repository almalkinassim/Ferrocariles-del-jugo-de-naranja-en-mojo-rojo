import classes
import graphics 
import tkinter as tkr
import random as rd

#no se si poner canvas en main o en graphics
root = tkr.Tk()
root.title("Ferrocariles del jugo de naranja")
canvas = tkr.Canvas(root, width=1024, height=786, bg= "#2F1939")
#buscar funcion pack
canvas.pack()
#canvas_resize = graphics.CanvasResize(canvas)
galaxie = classes.Galaxia() # ! esto es para iniciar la galaxia 
galaxie.SamsungGalaxy(20) # esto es para generar los planetas

sprites = []
for i in galaxie.listPlnt:
    sprites.append(graphics.PlanetSprite(canvas,i,f"Assets/planete_{rd.randint(1,8)}.png"))
    print(i)

#test avec tous, mais on peut faire tourner avec top 5 fitness ou similaire
n=10
ittest = classes.Itinerarios(galaxie)# que es ittest? te refieres a fittest?
ittest.genererRd(n)
routes = []

for i in range(n):
    route_lines = graphics.GalaxyPath(canvas, ittest.itinerarios[i])
    routes.append(route_lines)
    
    
fitness_list = []

for i in ittest.itinerarios:
    d = ittest.Dist(i)
    f = 1 / d
    fitness_list.append((i, f))

for chemin, fitness in fitness_list:
    print("Chemin :", chemin)
    print("Fitness :", fitness)
    print("Distance :",ittest.Dist(i) )
    print("--------------")


#graphics.GalaxyPath(canvas, galaxie) 


root.mainloop()
