import classes
import graphics 
import tkinter as tkr
import random as rd

#no se si poner canvas en main o en graphics
root = tkr.Tk()
root.title("Ferrocariles del jugo de naranja")
canvas = tkr.Canvas(root, width=900, height=700, bg= "#2F1939")
#buscar funcion pack
canvas.pack()
canvas_resize = graphics.CanvasResize(canvas)

#
#  galaxie = classes.Ititneraire.SamsungGalaxy(None,10)# ! esto es para obtener solo la lista de planetas, falta testearlo

sprites = []
for i in galaxie:
    sprites.append(graphics.PlanetSprite(canvas,i,f"Assets/planete_{rd.randint(1,8)}.png"))
    
#graphics.GalaxyPath(canvas, galaxie) 

root.mainloop()

#