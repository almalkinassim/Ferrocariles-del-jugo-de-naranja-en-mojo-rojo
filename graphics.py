import tkinter 
from PIL import Image, ImageTk 

class PlanetSprite:
  #canvas: afficher dans la fenetre, planet: coord, path: trouver l'image 
  def __init__(self,canvas,planet,path): 
    self.canvas = canvas
    self.planet = planet 
    # detallar como encontrar photo -> PIL.ImageTK no sirvio pero PIL.Image si ;-;
    img = Image.open(path) #charge image 
    imgsz = img.resize((64,64)) 
    self.photo = ImageTk.PhotoImage(imgsz) #la fait lisible pour tkinter
    # id Permet la visualisation dans la fenetre de tkinter
    self.id = canvas.create_image(planet.x,planet.y,image=self.photo)

class CanvasResize:
  def __init__(self,canvas):
    self.canvas = canvas
    self.canvas.bind("<Configure>", self.resize)
  def resize(self,event):
    # Redimensionne le canvas
    self.canvas.config(width=event.width, height=event.height)

def GalaxyPath(canvas,galaxy):
  for i in range(len(galaxy) - 1):
      p1 = galaxy[i]
      p2 = galaxy[i + 1]
      canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="white", width=2)